"""
1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
Uses basic if-else statements.
"""

score = float(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
