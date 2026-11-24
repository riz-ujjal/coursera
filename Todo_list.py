"""3. To-do list in the terminal (2-3 hours)
A menu with options to add a task, show tasks, mark one as done, and quit. Keep tasks in a Python list at first.

Practises: lists, dictionaries and functions."""

def add_task(tasks, title):
    # Use a boolean for status for easier management
    task = {"id": len(tasks) + 1, "title": title, "completed": False}
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is currently empty.")
        return
    
    print("\n--- Your To-Do List ---")
    for task in tasks:
        status = "[✔]" if task["completed"] else "[ ]"
        print(f"{task['id']}. {status} {task['title']}")
    print("----------------------")

def mark_task_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("Enter the task ID to mark as done: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task {task_id} marked as done!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        print("\n--- TODO MENU ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task Done")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            title = input("Enter the task title: ")
            add_task(tasks, title)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
