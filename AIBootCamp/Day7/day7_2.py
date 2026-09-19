# Task Manager Application

import os


# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from the file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[task_id] = {"title": title, "status": status}
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")     
            
# Add a new task
def add_task(tasks):
    task_id = str(len(tasks) + 1)
    title = input("Enter task title: ")
    tasks[task_id] = {"title": title, "status": "Pending"}
    save_tasks(tasks)
    print(f"Task '{title}' added with ID {task_id}.")
    
# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks:")
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")

# Update task status
def update_task_status(tasks):
    task_id = input("Enter task ID to update: ")
    if task_id in tasks:
        new_status = input("Enter new status (Pending/Completed): ")
        tasks[task_id]["status"] = new_status
        save_tasks(tasks)
        print(f"Task ID {task_id} status updated to '{new_status}'.")
    else:
        print(f"Task ID {task_id} not found.")
        
# Delete a task
def delete_task(tasks):
    task_id = input("Enter task ID to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print(f"Task ID {task_id} deleted.")
    else:
        print(f"Task ID {task_id} not found.")
        
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task_status(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()