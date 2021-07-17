student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
    score = student_scores[i]
    if score >= 91 and score <= 100:
        student_grades[i] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[i] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[i] = "Acceptable"
    elif score < 70:
        student_grades[i] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
