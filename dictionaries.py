# Dictionaries?
# Dictionaries use KEY VALUE pairs to save the data
# The data can be retrieved by its value or the key
# Syntax dict{} List[] Tuple()
# With in the dict we can also have list declared

# Let's create one
dev_ops_student = {
    "key": "value",
    "name": "James",
    "stream": "devops",
    "completed_lesson": 3,
    "completed_lessons_names": ["variables", "data types", "collections"]
    # key               value:     0             1               2
}
# print(dev_ops_student)
# # confirm the type
# # print(type(dev_ops_student))
#
# print(dev_ops_student["name"])
# print(dev_ops_student["completed_lesson"])
# print(dev_ops_student["completed_lessons_names"][1])
# print(dev_ops_student.keys())
# # print(dev_ops_student.values())
#
# # Add "operators" as a value of completed_lesson_names
# dev_ops_student["completed_lessons_names"].append("Operators")
# print(dev_ops_student)
#
# # Change the competed lesson from 3 to 4
# dev_ops_student["completed_lessons"] = 4
# print(dev_ops_student["completed_lessons"])
#
# # Remove the "data type" from completed_lesson_names
# dev_ops_student["completed_lessons_names"].remove("data types")
# print(dev_ops_student["completed_lessons_names"])

# Sets? The difference is that Sets are unordered
# Syntax {}
# Let's create a set

car_parts = {"wheels", " windows", "doors"}
print(car_parts)
print(type(car_parts))
car_parts.add("seats")
print(car_parts)
car_parts.discard("doors")
print(car_parts)
# Forzen sets - home work
