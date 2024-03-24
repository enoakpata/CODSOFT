tasks = {}

def create_task(task_description):
    tasks[len(tasks) + 1] = task_description

def delete_task(task_index):
    if task_index in tasks:
        del tasks[task_index]
    else:
        print("Task not found")

def display_tasks():
    if tasks:
        print("To-do list:")
        for task_index, task_description in tasks.items():
            print(f"{task_index}: {task_description}")
    else:
        print("To-do list is empty")

while True:
    print("\nMAIN MENU")
    print("1. Add task\n2. Remove task\n3. Display tasks\n4. Exit program")

    choice = input("What would you like to perform: ")

    if choice == '1':
        task_description = input("Enter a task: ")
        create_task(task_description)
    elif choice == '2':
        task_index = int(input("Enter task index to remove: "))
        delete_task(task_index)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
