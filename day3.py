# student = ("Lakshmi", 23, "AI")

# print(student)
# print(student[0])
# print(type(student))


"""Tuple Unpacking"""
# name, age, field = student

# print(name)
# print(age)
# print(field)


"""Task 1:
student = ("Ananya", 21, "CSE", 8.5)
Print name and CGPA
Try to change CGPA (see the error)
Unpack tuple into variables"""

# student = ("Ananya", 21, "CSE", 8.5)

# print("NAME:", student[0])
# print("CGPA:", student[3])

# try:
#     student[3] = 9.0
# except TypeError as e:
#     print("Error:", e)

"""to change the elements in the tuple first we need to change the tuple into list than we can change 
tuple into list"""
# student_list = list(student)
# student_list[3] = 9.0
# student = tuple(student_list)
# print("Updated tuple:", student)

# name, age, branch, cgpa = student

# print("unpacked values:")
# print("Name:", name)
# print("Age:", age)
# print("Branch:", branch)
# print("CGPA:", cgpa)

"""Task 2:
Create a tuple of 5 numbers
Print max & min
Count how many times a number appears
Reverse the tuple"""

# numbers = (10, 20, 30, 20, 40)

# print("Maximum:", max(numbers))
# print("Minimum:", min(numbers))

# print("count of 20:", numbers.count(20))

# reverse_tuple = numbers[::-1]
# print("Reversed_tuple:", reverse_tuple)

"""Task 3:
nums = [1,2,3,2,4,3,5]
Convert list to set
Remove duplicates
Convert back to list"""


# nums = [1, 2, 3, 2, 4, 3, 5]

# nums_set = set(nums)
# print("Nums_set:", nums_set)

# unique_nums = list(nums_set)
# print("Unique_nums:", unique_nums)


"""Task 4
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Common elements
Elements only in A
Elements only in B
All unique elements"""

# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

# #intersection  it returns only common elements in the both sets
# common = A & B
# print("Common elements:", common)

# # difference it returns only the elememts present in the A set
# only_in_A = A - B
# print("Elements only in A:", only_in_A)

# #difference it returns only the elememts present in the B set
# only_in_B = B - A
# print("Elements only in B:", only_in_B)

# # union it returns the all elements in both sets doesn't allow duplicates
# all_unique = A | B
# print("All unique elements:", all_unique)


"""Task 5:
You are tracking unique email IDs registering on a site.
emails = [
 "a@gmail.com",
 "b@gmail.com",
 "a@gmail.com",
 "c@gmail.com"
]
Find unique emails
Count total unique users"""

# emails = [
#     "a@gmail.com",
#     "b@gmail.com",
#     "a@gmail.com",
#     "c@gmail.com"
# ]

# unique_emails = set(emails)
# print("Unique emails:", unique_emails)

# print("Total unique users:", len(unique_emails))


"""Task 6
data = [
 ("Lakshmi", "Python"),
 ("Rahul", "Java"),
 ("Lakshmi", "Python"),
 ("Anita", "Python")
]
Find unique students
Find unique courses
Count how many students chose Python"""

# data = [
#     ("Lakshmi", "Python"),
#     ("Rahul", "Java"),
#     ("Lakshmi", "Python"),
#     ("Anita", "Python")
# ]

# unique_students = {student for student, course in data}
# print("Unique students:", unique_students)

# unique_courses = {course for student, course in data}
# print("Unique courses:", unique_courses)

# python_count = sum(1 for student, course in data if course == "Python")
# print("Number of students who chose Python:", python_count)

"""Task 7
 Create a tuple with model name, accuracy, and training time
 Access each element
 Try to modify it (see the error)"""

# model_info = ("ResNet50", 0.92, "2 hours")


# print("Model Name:", model_info[0])
# print("Accuracy:", model_info[1])
# print("Training Time:", model_info[2])

# model_info[1] = 0.95

"""Task 8
result = ("SVM", 0.89, 120)
# Unpack and print:
# Model: SVM
# Accuracy: 0.89
# Time: 120 sec"""

# result = ("SVM", 0.89, 120)

# model, accuracy, time = result

# print("Model:", model)
# print("Accuracy:", accuracy)
# print("Time:", time, "sec")

"""Task 9
# Create a tuple for dataset shape (rows, columns)
# Write code to print:
# "Dataset has X rows and Y features"""


# dataset_shape = (1000, 20)   #  1000 rows, 20 columns

# rows, columns = dataset_shape

# print(f"Dataset has {rows} rows and {columns} features")

"""Task 10
labels = [1, 0, 1, 1, 0, 2, 2]
# Convert to set
# Print unique labels"""

# labels = [1, 0, 1, 1, 0, 2, 2]

# unique_labels = set(labels)

# print("Unique labels:", unique_labels)

"""Task 11
train_features = {"age", "salary", "experience", "dept"}
test_features = {"age", "salary", "location"}
# Find:
# 1. Common features
# 2. Missing in test
# 3. Extra in test
"""

# train_features = {"age", "salary", "experience", "dept"}
# test_features = {"age", "salary", "location"}

# common = train_features & test_features
# print("Common features:", common)

# # (present in train but not in test)
# missing_in_test = train_features - test_features
# print("Missing in test:", missing_in_test)

# # (present in test but not in train)
# extra_in_test = test_features - train_features
# print("Extra in test:", extra_in_test)

"""task 12
text = "AI and ML are part of AI"
# Find unique words using set"""

# text = "AI and ML are part of AI"

# words = text.split()

# unique_words = set(words)

# print("Unique words:", unique_words)

"""task 13
models = [("LR", 0.82), ("SVM", 0.89), ("RF", 0.85)]
# 1. Convert model names to a set
# 2. Find the best model using tuple logic"""

# models = [("LR", 0.82), ("SVM", 0.89), ("RF", 0.85)]

# model_names = set([m[0] for m in models])
# print("Model names set:", model_names)

# best_model = models[0]   # assume first is best
# for m in models:
#     if m[1] > best_model[1]:
#         best_model = m

# print("Best model:", best_model[0], "with accuracy", best_model[1])