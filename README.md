# Todo CLI App

A simple command-line task manager written in Python.

Todo CLI App allows you to manage your tasks directly from the terminal. You can create, update, remove, list, and change the status of tasks. All tasks are stored locally in a JSON file, so your data persists between sessions.

## ✨ Features

- Add new tasks
- Update task descriptions
- Remove tasks by ID
- Mark tasks as in-progress
- Mark tasks as done
- List all tasks
- Filter tasks by status:
  - to-do
  - in-progress
  - done
- Built-in help command
- Automatic task ID generation
- Task creation and update timestamps
- Local JSON storage
- Input validation for task IDs and descriptions

## 📁 Project Structure

```text
.
├── todo.py
├── todo_help.py
├── todo_data.json
├── .gitignore
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/danielmascian/tdo-cli.git
```

Move into the project directory:

```bash
cd tdo-cli
```

Run the application:

```bash
python3 todo.py help
```

## 📖 Commands

### Add a task

```bash
python3 todo.py add Learn Python
```

### Update a task

```bash
python3 todo.py update 1 Learn Python Every Day
```

### Remove a task

```bash
python3 todo.py remove 1
```

### Mark a task as in progress

```bash
python3 todo.py mark-in-progress 1
```

### Mark a task as done

```bash
python3 todo.py mark-done 1
```

### List all tasks

```bash
python3 todo.py list
```

### List only todo tasks

```bash
python3 todo.py list-todo
```

### List only in-progress tasks

```bash
python3 todo.py list-in-progress
```

### List only completed tasks

```bash
python3 todo.py list-done
```

### Show help

```bash
python3 todo.py help
```

## 📋 Example Output

```text
[1] Learn Python
  Status : to-do
  Created: 2026-06-26 15:20:10
  Updated: 2026-06-26 15:20:10
```

## 💾 Data Storage

Tasks are stored in a local JSON file named `todo_data.json`.

Each task contains:

- ID
- Description
- Status
- Created timestamp
- Updated timestamp

## 💡 Inspiration

This project was built as my solution to the **Task Tracker** project from **roadmap.sh**.

The goal was to practice Python by building a command-line application that uses file handling, JSON, functions

Project page: https://roadmap.sh/projects/task-tracker
