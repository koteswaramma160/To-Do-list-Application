# ===================== Task Class =====================
import json
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True


# ===================== File Handling =====================
def save_tasks(tasks):
    with open("tasks_todo.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open("tasks_todo.json", "r") as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []


# ===================== Menu Functions =====================
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter category (Work/Personal/Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task.completed else "❌"
            print(f"{i}. {task.title} ({task.category}) - {status}")
            print(f"   Description: {task.description}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task index to mark completed: "))
        tasks[idx].mark_completed()
        print("✅ Task marked as completed!")
    except (ValueError, IndexError):
        print("❌ Invalid index.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task index to delete: "))
        removed = tasks.pop(idx)
        print(f"🗑 Deleted task: {removed.title}")
    except (ValueError, IndexError):
        print("❌ Invalid index.")


# ===================== Main Program =====================
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! ✅")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()



