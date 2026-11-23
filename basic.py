import json
from pathlib import Path


DATA_FILE = Path("tasks.json")
VALID_PRIORITIES = ("low", "medium", "high")


def load_tasks():
    """Load tasks from the local JSON file, handling missing or malformed files gracefully."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print("Warning: tasks.json did not contain a list. Starting with an empty list.")
            return []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read tasks.json (file may be malformed). Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list to the local JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2)
        print("Tasks saved successfully.")
    except OSError as error:
        print(f"Error saving tasks: {error}")


def add_task(tasks):
    """Collect and validate a task description and priority, then append to tasks."""
    description = input("Task description: ").strip()
    if not description:
        print("Description cannot be blank.")
        return

    priority = input("Priority (low/medium/high) [medium]: ").strip().lower()
    if not priority:
        priority = "medium"
    elif priority not in VALID_PRIORITIES:
        print("Invalid priority. Defaulting to 'medium'.")
        priority = "medium"

    tasks.append({
        "description": description,
        "done": False,
        "priority": priority,
    })
    print(f"Added task: '{description}' (priority: {priority}).")


def list_tasks(tasks):
    """Display all tasks with their number, completion status, priority, and description."""
    if not tasks:
        print("No tasks yet.")
        return

    print("\n--- Current Tasks ---")
    for index, task in enumerate(tasks, start=1):
        marker = "x" if task.get("done") else " "
        priority = task.get("priority", "medium")
        description = task.get("description", "")
        print(f"{index}. [{marker}] ({priority}) {description}")


def get_valid_task_number(tasks, prompt_text="Task number: "):
    """Validate that tasks exist and that the user enters a valid 1-based task number."""
    if not tasks:
        print("No tasks available.")
        return None

    raw = input(prompt_text).strip()
    if not raw.isdigit():
        print("Enter a whole-number task number.")
        return None

    number = int(raw)
    if not 1 <= number <= len(tasks):
        print("That task number does not exist.")
        return None

    return number


def complete_task(tasks):
    """Mark a validated task number as complete."""
    number = get_valid_task_number(tasks, "Task number to complete: ")
    if number is None:
        return

    task = tasks[number - 1]
    task["done"] = True
    print(f"Completed task {number}: '{task.get('description', '')}'.")


def delete_task(tasks):
    """Delete a validated task number from the list."""
    number = get_valid_task_number(tasks, "Task number to delete: ")
    if number is None:
        return

    removed = tasks.pop(number - 1)
    print(f"Deleted task {number}: '{removed.get('description', '')}'.")


def main():
    tasks = load_tasks()
    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save now")
        print("6. Exit")
        choice = input("Choose 1-6: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
