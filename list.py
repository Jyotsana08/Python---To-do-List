import datetime

class Task:
    def __init__(self, name, priority, due_date):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [t for t in self.tasks if t.name != task_name]

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                break

    def display_tasks(self):
        for task in self.tasks:
            print(f"{task.name} - Priority: {task.priority}, Due Date: {task.due_date}, Completed: {task.completed}")

def save_tasks(tasks, file_name):
    with open(file_name, 'w') as file:
        for task in tasks:
            file.write(f"{task.name},{task.priority},{task.due_date},{task.completed}\n")

def load_tasks(file_name):
    tasks = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                task_data = line.strip().split(',')
                task = Task(task_data[0], task_data[1], task_data[2])
                task.completed = task_data[3] == 'True'
                tasks.append(task)
    except FileNotFoundError:
        pass

    return tasks

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks("tasks.txt")

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Complete Task\n4. Display Tasks\n5. Save and Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(name, priority, due_date)
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            name = input("Enter task name to remove: ")
            task_manager.remove_task(name)
            print("Task removed successfully!")

        elif choice == "3":
            name = input("Enter task name to mark as completed: ")
            task_manager.complete_task(name)
            print("Task marked as completed!")

        elif choice == "4":
            task_manager.display_tasks()

        elif choice == "5":
            save_tasks(task_manager.tasks, "tasks.txt")
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()