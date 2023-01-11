student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Niraj": 79,
    "Bob":62,
    "Ben":0,
    "Neymar":15,
    
}
# 🚨 Don't change the code above 👆

student_grades = {}
for name, score  in student_scores.items():
    if score >= 91 and score <= 100:
        student_grades[name] = "outstanding"
    elif score >= 81 and score <= 90:
        student_grades[name] = "exceed expectation"
    elif score >= 71 and score <= 80:
        student_grades[name] = "acceptable"
    else:
        student_grades[name] = "fail"



        
        

# TODO-1: Create an empty dictionary called student_grades.
# score_to_grade = {
#     range(91,101): "outstanding",
#     range(81,91):"exceed expectation",
#     range(71,81):"acceptable",
#     range(0,71):"fail"
#     }
# student_grades = {}


# # TODO-2: Write your code below to add the grades to student_grades.👇

# for name, score in student_scores.items():
#     print(name, score)

#     for score_range in score_to_grade:
#         if score in score_range:

#             student_grades[name] = score_to_grade[score_range]

#     student_grades["Harry"] = "exceeds expectations"
# student_grades["Ron"] = "acceptable"
# student_grades["Hermione"] = "outstanding"
# student_grades["Draco"] = "acceptable"
# student_grades["Neville"] = "fail"

# 🚨 Don't change the code below 👇

print(student_grades)
