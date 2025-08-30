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
├── tasks.json       # Stores tasks data (created automatically)
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

---

## 🛠 Requirements
- Python 3.x  
- No external libraries needed (only built-in `json` module)

---

## 📝 Future Enhancements
- 🔍 Search tasks by keyword or category
- 📊 Filter by completed/pending
- 📅 Due dates & reminders
- 🌐 GUI or Web version

---

## 👨‍💻 Author
Developed as a beginner-friendly **Python CLI project** to practice:
- Object-Oriented Programming (OOP)
- File handling with JSON
- Menu-driven console apps
*/





Topic: Classifying the noises from a ballast image by identifying the voids under sleepers using AI (Mask R-CNN or YOLACT)
Core idea: The amount, size, and distribution of voids in the ballast beneath sleepers correlate with noise generation and vibration when trains pass. By detecting these voids from images, we can classify noise severity levels.

🛠 Roadmap
Phase 1: Literature & Problem Framing

Background study

Review works on ballast voids, unsupported sleepers, and noise/vibration causes (e.g., Sysyn et al. 2021, Bojarczak et al. 2024).

Study image-based ballast analysis methods (fouling detection, sleeper detection, unevenness).

Problem definition

Goal: Map void features → noise levels.

Assumption: Larger/more voids = higher noise impact.

Phase 2: Data Collection

Image data

Capture real-time images of ballast under sleepers (day/night, various conditions).

Use synthetic augmentation (rotation, brightness, scaling) to expand dataset.

Optionally use MDPI’s ballast dataset as a base.

Noise data

Record noise/vibration levels simultaneously with images (if possible).

Otherwise, simulate labels (e.g., “low noise = <10% void area,” “medium noise = 10–30%,” “high noise = >30% voids”).

Phase 3: Void Detection Model

Annotation

Manually label voids (polygon masks) in a subset of images.

Classes: ballast, sleeper, void.

Model training

Mask R-CNN (accuracy-oriented, strong for irregular shapes).

YOLACT (real-time oriented).

Evaluate precision/recall for void detection.

Post-processing

Calculate area, distribution, % coverage of voids.

Derive void features: total void area, average void size, location (under sleeper vs side ballast).

Phase 4: Noise Classification

Feature engineering

Use detected void statistics as input to classifier:

total_void_area

mean_void_size

void_density_under_sleeper

void_position_ratio (under vs side)

Combine with metadata (train speed, axle load, etc. if available).

Classifier

Train ML/DL models:

Classical: Random Forest, SVM (if features only).

Deep: A small CNN/MLP (if using raw images + void masks).

Target output: Noise severity classes (low, medium, high).

Phase 5: System Integration

Pipeline

Input: Real-time ballast image.

Step 1: Void detection (Mask R-CNN / YOLACT).

Step 2: Feature extraction (void size/area/location).

Step 3: Noise classification (ML/DL classifier).

Output: Predicted noise level + annotated image.

Visualization

Show ballast image with void contours and labeled noise severity.

Optionally log statistics for maintenance engineers.

Phase 6: Evaluation & Validation

Accuracy metrics

Void detection: IoU, mAP (segmentation accuracy).

Noise classification: Precision, Recall, F1, Confusion Matrix.

Validation

Compare predicted noise levels vs actual measured noise/vibration (if data collected).

Conduct ablation study: Mask R-CNN vs YOLACT, feature-based vs image-based.

Phase 7: Deployment

Prototype app (Flask/Streamlit dashboard).

Upload an image → system highlights voids → system predicts expected noise impact level.

Optionally connect to track-side monitoring systems.

🔑 Deliverables

Dataset (images of ballast voids + labels).

Trained Mask R-CNN or YOLACT model.

Noise classification model.

End-to-end pipeline with results visualization.

Research report (linking void detection to noise).

⚡ Summary:
You will build a vision-based monitoring system: detect voids beneath sleepers → compute void features → classify noise severity.
This project bridges image segmentation (Mask R-CNN / YOLACT) with noise impact analysis, making it both AI research and practical railway engineering.
