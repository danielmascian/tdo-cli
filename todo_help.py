def help_command() -> None:
    print("""
Todo CLI

Usage:
    python main.py <command> [arguments]

Commands:
    add <description>              Add a new task
    update <id> <description>      Update a task description
    remove <id>                    Remove a task
    mark-in-progress <id>          Mark a task as in progress
    mark-done <id>                 Mark a task as completed
    list                           List all tasks
    list-todo                      List tasks with status 'to-do'
    list-in-progress               List tasks with status 'in-progress'
    list-done                      List tasks with status 'done'
    help                           Show this help message

Examples:
    python main.py add "Learn Python"
    python main.py update 1 "Learn Python OOP"
    python main.py remove 1
    python main.py mark-in-progress 2
    python main.py mark-done 2
    python main.py list
    python main.py list-done
""")