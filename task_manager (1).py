
import json
from datetime import datetime
from tabulate import tabulate

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_dict['title'],
            task_dict['description'],
            task_dict['due_date'],
            task_dict['priority']
        )

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, description, due_date, priority):
        new_task = Task(title, description, due_date, priority)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        task_table = []
        for idx, task in enumerate(self.tasks, 1):
            task_table.append([
                idx, task.title, task.description, task.due_date, task.priority
            ])
        print(tabulate(task_table, headers=["ID", "Title", "Description", "Due Date", "Priority"]))

    def update_task(self, task_id, title=None, description=None, due_date=None, priority=None):
        if task_id > len(self.tasks) or task_id < 1:
            print("Invalid task ID.")
            return
        task = self.tasks[task_id - 1]
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if priority:
            task.priority = priority
        self.save_tasks()
        print("Task updated successfully!")

    def delete_task(self, task_id):
        if task_id > len(self.tasks) or task_id < 1:
            print("Invalid task ID.")
            return
        del self.tasks[task_id - 1]
        self.save_tasks()
        print("Task deleted successfully!")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                task_data = json.load(file)
                return [Task.from_dict(task) for task in task_data]
        except FileNotFoundError:
            return []

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (Low, Medium, High): ")
            task_manager.add_task(title, description, due_date, priority)

        elif choice == '2':
            task_manager.view_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (leave blank to keep current): ")
            priority = input("Enter new priority (leave blank to keep current): ")
            task_manager.update_task(task_id, title, description, due_date, priority)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
