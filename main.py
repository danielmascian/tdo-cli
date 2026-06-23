import json
import os
import sys
from datetime import datetime
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

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


def next_id(tasks: list) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add(tasks: list, task_description: str) -> dict:
    now = datetime.now().isoformat()
    new_task = {
        "id": next_id(tasks),
        "description": task_description,
        "status": Status.ACTIVE.value,
        "created_at": now,
        "updated_at": now,
    }
    tasks.append(new_task)
    print(f"Task added successfully (ID: {new_task["id"]})")
    return new_task


def debug(tasks: list) -> None:
    for task in tasks:
        print(task)


def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [arguments]")
        sys.exit(1)

    task_function = sys.argv[1]
    tasks = load_tasks()

    match task_function:
        case "add":
            task_description = sys.argv[2]
            add(tasks, task_description)
            save_tasks(tasks)
        case _:
            print(f"Unknown command: {task_function}")
            sys.exit(1)

    #debug(tasks)


if __name__ == "__main__":
    main()