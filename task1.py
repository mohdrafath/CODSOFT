# Task 1 - To-do list
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    task_description = input("Enter task description: ")
    tasks.append({"task": task_description, "completed": False})
    print(f"Task '{task_description}' added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found!\n")
        return
    
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['task']}")
    print()

def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark as complete!\n")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]["completed"] = True
            print(f"Task {task_num} marked as complete!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!\n")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num-1)
            print(f"Task '{removed_task['task']}' deleted successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1-5.\n")

if __name__ == "__main__":
    main()
