# Task Manager CLI

A simple and efficient command-line interface (CLI) task manager built in Python, allowing users to manage their tasks with ease. This application lets you add, update, view, and delete tasks. Tasks are saved to a JSON file, ensuring persistence across sessions.

## Features
- **Add Tasks**: Create tasks by specifying the title, description, due date, and priority.
- **View Tasks**: Display a list of all tasks in a table format with their details.
- **Update Tasks**: Modify the title, description, due date, or priority of existing tasks.
- **Delete Tasks**: Remove tasks by specifying their ID.
- **Persistent Data**: Tasks are stored in a `tasks.json` file for data persistence across sessions.
- **Organized Task List**: Tasks are displayed in an organized, readable table using the `tabulate` library.

## Installation

### Prerequisites
- Python 3.x

### Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/task-manager-cli.git
    ```
2. Navigate to the project folder:
    ```bash
    cd task-manager-cli
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, run the application by executing the following command:

```bash
python task_manager.py
Available Options:
1. Add Task: Create a new task by entering the task details when prompted.
2. View Tasks: View a list of all tasks with their ID, title, description, due date, and priority.
3. Update Task: Update an existing task by entering its ID and the new values.
4. Delete Task: Remove a task by entering its ID.
5. Exit: Exit the application.
Example Usage:
bash
Copy
Task Manager Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: Buy groceries
Enter task description: Buy milk, bread, and eggs
Enter due date (YYYY-MM-DD): 2025-01-30
Enter task priority (Low, Medium, High): Medium
Task added successfully!

Choose an option: 2
ID    Title         Description                Due Date   Priority
----  ------------  -------------------------- ---------- --------
1     Buy groceries Buy milk, bread, and eggs  2025-01-30 Medium
