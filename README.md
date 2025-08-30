/*
# 📝 Personal To-Do List (Python CLI)

A simple **command-line To-Do List application** built with Python.  
This project allows you to add, view, complete, and delete tasks, while saving them in a JSON file for persistence.

---

## 📌 Features
- ➕ **Add Task** – Add new tasks with title, description, and category (Work/Personal/Urgent).
- 👀 **View Tasks** – View all tasks with their details and completion status.
- ✅ **Mark as Completed** – Mark tasks as done.
- 🗑 **Delete Task** – Remove tasks from the list.
- 💾 **Persistent Storage** – All tasks are stored in `tasks.json` so they remain even after restarting the program.

---

## ⚙️ How It Works
1. Tasks are stored as objects of the `Task` class.
2. Each task has:
   - **title** → Short name of the task  
   - **description** → Detailed info about the task  
   - **category** → Work, Personal, or Urgent  
   - **completed** → Boolean status (default `False`)  
3. When the program exits, tasks are **saved to `tasks.json`**.  
4. When restarted, tasks are **loaded back** from `tasks.json`.  

---

## 📂 Project Structure
```
.
├── tasks_todo.json       # Stores tasks data (created automatically)
├── todo.py          # Main program
└── README.md        # Documentation
```

---

## 🚀 Usage

### 1️⃣ Run the Program
```bash
python todo.py
```

### 2️⃣ Menu Options
```
--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
```

### 3️⃣ Example
```
--- Personal To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
Choose an option: 1
Enter task title: Finish Report
Enter task description: Complete the monthly sales report
Enter category (Work/Personal/Urgent): Work
✅ Task added successfully!
```
-------------
