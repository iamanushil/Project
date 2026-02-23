# A2: Python and Bash — Assignment

This folder contains four Python programs for the assignment.

---

## 1. Grade Checker (`1_grade_checker.py`)

Takes a score as input and prints the grade using **if-else**:

- **90+** → "A"
- **80–89** → "B"
- **70–79** → "C"
- **60–69** → "D"
- **Below 60** → "F"

**Run:**
```bash
cd "A2: Python And Bash"
python3 1_grade_checker.py
```
Then enter a number when prompted (e.g. `85` → B).

---

## 2. Student Grades (`2_student_grades.py`)

Uses a **dictionary** (keys = student names, values = grades) and a simple menu:

- **1** — Add a new student and grade  
- **2** — Update an existing student’s grade  
- **3** — Print all student grades  
- **4** — Exit  

**Run:**
```bash
python3 2_student_grades.py
```

---

## 3. Write to a File (`3_write_to_file.py`)

Creates a text file and writes content using **`open()`** and **`write()`**.

**Run:**
```bash
python3 3_write_to_file.py
```
This creates `sample_content.txt` in the same folder.

---

## 4. Read from a File (`4_read_from_file.py`)

Opens the file in **read mode** and uses **`file.read()`** to read and **`print()`** the content.

**Run (after running program 3 so the file exists):**
```bash
python3 4_read_from_file.py
```

---

## Submission Guidelines

- Attach **screenshots** or **terminal commands** with brief **explanations**.
- Submit in **Google Doc** or **Microsoft Word**, or share a **GitHub link** to this folder.

### Suggested doc content

1. **Grade Checker** — Screenshot/command of running `1_grade_checker.py` with 2–3 sample scores and a short note: “Uses if-else to map score ranges to letter grades.”
2. **Student Grades** — Screenshot/command showing: add student, update grade, print all; note: “Uses a dictionary and if-else for menu and validation.”
3. **Write to a File** — Screenshot/command of `3_write_to_file.py` and the created `sample_content.txt`; note: “Uses `open()` and `write()` to create and write to the file.”
4. **Read from a File** — Screenshot/command of `4_read_from_file.py` output; note: “Uses `open()` in read mode and `file.read()` to read and print the file.”
