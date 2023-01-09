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

for students_grades in student_scores:

    student_grades["Harry"] = "exceeds expectations"
student_grades["Ron"] = "acceptable"
student_grades["Hermione"] = "outstanding"
student_grades["Draco"] = "acceptable"
student_grades["Neville"] = "fail"

# 🚨 Don't change the code below 👇

print(student_grades)
