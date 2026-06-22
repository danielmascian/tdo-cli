import json
import os
import sys
from datetime import datetime
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

def add(task_properties : dict,task_description : str) -> dict:
    print("Working add function")

def debug(task_properties : dict) -> dict:
    for key,value in task_properties.items():
        print(key , ":" , value)

def start_program():
    print("Welcome!")

def main():
    start_program()

    if len(sys.argv) < 2:
        print("Usage: main.py <command> [arguments]")
        sys.exit(1)
    
    task_function = sys.argv[1]
    task_description = sys.argv[2]

    task_properties = { 
        "id": 1,
        "description": task_description,
        "status": Status.ACTIVE.value,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    match task_function:
        case "add":
            add(task_properties,task_description)   
    

    debug(task_properties)
    
    '''
    if os.path.exists("todo_data.json"):
        print("File exists")
        with open("todo_data.json", "r") as f:
            data = json.load(f)
        print(data)
    else:
        print("File does not exist")
        data = []  

    return data
    '''
if __name__ == "__main__":
    main()