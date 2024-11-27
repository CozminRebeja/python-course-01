students = [
{"name": "Alice", "grade": 88},
{"name": "Bob", "grade": 45},
{"name": "Charlie", "grade": 67},
{"name": "David", "grade": 30},
{"name": "Eve", "grade": 55}
]

name_list = [x["name"] for x in students]
grade_list = []

# dict(zip(list1, list2))
for i in students:
    if i["grade"] >= 50:
        grade_list.append("Pass")
    else:
        grade_list.append("Fail")

final_list = list(zip(name_list, grade_list))
print(final_list)

