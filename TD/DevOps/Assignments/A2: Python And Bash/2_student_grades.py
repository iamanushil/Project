"""
2. Student Grades
Dictionary: keys = student names, values = grades.
User can: Add new student and grade, Update existing grade, Print all grades.
Uses dictionary and basic operations with if-else.
"""

student_grades = {}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        if name in student_grades:
            print(f"Student '{name}' already exists. Use option 2 to update.")
        else:
            grade = input("Enter grade: ").strip()
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ").strip()
        if name in student_grades:
            new_grade = input("Enter new grade: ").strip()
            student_grades[name] = new_grade
            print(f"Updated {name}'s grade to {new_grade}.")
        else:
            print(f"Student '{name}' not found. Use option 1 to add.")

    elif choice == "3":
        if not student_grades:
            print("No students in the list.")
        else:
            print("\n--- All Student Grades ---")
            for name, grade in student_grades.items():
                print(f"  {name}: {grade}")

    elif choice == "4":
        print("Exiting.")
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")
