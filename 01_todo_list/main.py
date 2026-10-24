tasks = []

FILE_NAME = "task.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task = line.strip()

                if task != "":
                    tasks.append(task)

    except FileNotFoundError:
        print("No saved tasks found. Starting a new list.")

def save_task():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_task():
    if len(tasks) == 0:
        print("\nYour task list is empty.")
    else:
        print("\n---------- Your Task ------------")
        for index in range(len(tasks)):
            print(f"{index + 1}. {tasks[index]}")


def add_task():
    task = input("Enter a task: ")

    if task != "":
        tasks.append(task)
        save_task()
        print("Task Added")
    else:
        print("Task cannot be empty.")

def remove_task():
    show_task()

    if len(tasks) > 0:
        task_number = input("\nEnter task number to remove: ")

        if task_number.isdigit():
            task_number = int(task_number)

            if task_number >= 1 and task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                save_task()
                print(f"Removed: {removed_task}")
            else:
                print("That task number dose note exit.")
        else:
            print("Please enter a number.")

load_tasks()

def clear_tasks():
    if len(tasks) == 0:
        print("Your task list is already empty.")
        return

    confirmation = input("Delete every task? (yes/no): ")

    if confirmation.lower() == "yes":
        tasks.clear()
        save_task()
        print("All tasks were deleted.")
    else:
        print("Nothing was deleted.")


while True:
    print("\n----- To-Do List -----")
    print("1. Show task ")
    print("2. Add task")
    print("3. Remove task")
    print("4. Clear all Tasks")
    print("5. Exit")

    choice = input("Choosean option: ")

    if choice == "1":
        show_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("GoodByr!")
        break
    else:
        print("Invalid option. Try again.")

