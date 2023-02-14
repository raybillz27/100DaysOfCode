import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [65, 80, 59]
}

# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(value)
for (index, row) in student_data_frame.iterrows():
    print(row)
