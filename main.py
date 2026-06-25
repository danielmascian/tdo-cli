import json
import os
import sys
from datetime import datetime
from enum import Enum


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


def check_list(tasks: list) -> bool:
    if not tasks:
        print("List is empty.")
        return False
    return True


def next_id(tasks: list) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add(tasks: list, task_description: str) -> dict:
    now = datetime.now().isoformat()

    new_task = {
        "id": next_id(tasks),
        "description": task_description,
        "status": Status.TODO.value,
        "created_at": now,
        "updated_at": now,
    }

    tasks.append(new_task)
    print(f"Task added successfully (ID: {new_task['id']})")
    return new_task


def remove(tasks: list, task_id: int) -> bool:
    if not check_list(tasks):
        return False

    original_length = len(tasks)
    tasks[:] = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == original_length:
        print(f"No task found with ID: {task_id}")
        return False

    print(f"Task removed successfully (ID: {task_id})")
    return True


def update(tasks: list, task_id: int, task_description: str) -> bool:
    if not check_list(tasks):
        return False

    now = datetime.now().isoformat()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = task_description
            task["updated_at"] = now
            print(f"Task updated successfully (ID: {task_id})")
            return True

    print(f"No task found with ID: {task_id}")
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [arguments]")
        sys.exit(1)

    task_function = sys.argv[1]
    tasks = load_tasks()

    match task_function:
        case "add":
            if len(sys.argv) < 3:
                print("Usage: main.py add <task_description>")
                sys.exit(1)

            task_description = sys.argv[2]
            add(tasks, task_description)
            save_tasks(tasks)
        case "remove":
            if len(sys.argv) < 3:
                print("Usage: main.py remove <task_id>")
                sys.exit(1)

            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number.")
                sys.exit(1)

            changed = remove(tasks, task_id)

            if changed:
                save_tasks(tasks)
        case "update":
            if len(sys.argv) < 4:
                print("Usage: main.py update <task_id> <new_description>")
                sys.exit(1)

            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number.")
                sys.exit(1)

            task_description = sys.argv[3]
            changed = update(tasks, task_id, task_description)

            if changed:
                save_tasks(tasks)
        case _:
            print(f"Unknown command: {task_function}")
            sys.exit(1)


if __name__ == "__main__":
    main()