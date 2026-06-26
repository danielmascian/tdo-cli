import json
import os
import sys
from datetime import datetime
from enum import Enum
from todo_help import help_command

class Status(Enum):
    TODO = "to-do"
    ACTIVE = "in-progress"
    COMPLETED = "done"


DATA_FILE = "todo_data.json"


def load_tasks() -> list:
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: {DATA_FILE} is corrupted, starting fresh.")
                return []
    return []


def save_tasks(tasks: list) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def require_args(count: int, usage: str) -> None:
    if len(sys.argv) < count:
        print(f"Usage: {usage}")
        print("Run 'python3 main.py help' to see all available commands.")
        sys.exit(1)

def get_task_id() -> int:
    require_args(3, "main.py <command> <task_id>")

    try:
        return int(sys.argv[2])
    except ValueError:
        print("Task ID must be a number.")
        sys.exit(1)

def validate_description(description: str) -> str:
    description = description.strip()

    if not description:
        print("Task description cannot be empty.")
        sys.exit(1)

    return description

def check_list(tasks: list) -> bool:
    if not tasks:
        print("List is empty.")
        return False
    return True


def next_id(tasks: list) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add(tasks: list, description: str) -> bool:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id": next_id(tasks),
        "description": description,
        "status": Status.TODO.value,
        "created_at": now,
        "updated_at": now,
    }

    tasks.append(task)
    print(f"Task added successfully (ID: {task['id']})")
    return True


def remove(tasks: list, task_id: int) -> bool:
    if not check_list(tasks):
        return False

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task removed successfully (ID: {task_id})")
            return True

    print(f"No task found with ID: {task_id}")
    return False


def update(tasks: list, task_id: int, description: str) -> bool:
    if not check_list(tasks):
        return False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Task updated successfully (ID: {task_id})")
            return True

    print(f"No task found with ID: {task_id}")
    return False


def mark_status(tasks: list, task_id: int, status: Status) -> bool:
    if not check_list(tasks):
        return False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status.value
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Task marked as {status.value} (ID: {task_id})")
            return True

    print(f"No task found with ID: {task_id}")
    return False

def list_all(tasks: list, status: Status | None = None) -> bool:
    if not check_list(tasks):
        return False

    found = False

    for task in tasks:
        if status is None or task["status"] == status.value:
            print(f"[{task['id']}] {task['description']}\n"
                f"  Status : {task['status']}\n"
                f"  Created: {task['created_at']}\n"
                f"  Updated: {task['updated_at']}\n")
            found = True

    if not found:
        print(f"No tasks found with status: {status.value}")

    return found
    

def main():
    require_args(2, "main.py <command> [arguments]")

    command = sys.argv[1]
    tasks = load_tasks()
    changed = False

    match command:
        case "add":
            require_args(3, "main.py add <task_description>")
            description = validate_description(" ".join(sys.argv[2:]))
            changed = add(tasks, description)

        case "remove":
            changed = remove(tasks, get_task_id())

        case "update":
            require_args(4, "main.py update <task_id> <new_description>")
            description = validate_description(" ".join(sys.argv[3:]))
            changed = update(tasks, get_task_id(), description)

        case "mark-in-progress":
            changed = mark_status(tasks, get_task_id(), Status.ACTIVE)

        case "mark-done":
            changed = mark_status(tasks, get_task_id(), Status.COMPLETED)
        case "list":
            list_all(tasks)

        case "list-todo":
            list_all(tasks, Status.TODO)

        case "list-in-progress":
            list_all(tasks, Status.ACTIVE)

        case "list-done":
            list_all(tasks, Status.COMPLETED)
        case "help":
            help_command()
        case _:
            print(f"Unknown command: {command}")
            print("Run 'python3 main.py help' to see all available commands.")
            sys.exit(1)

    if changed:
        save_tasks(tasks)


if __name__ == "__main__":
    main()