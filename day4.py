#  Dictionaries and conditions

# student = {
#     "name": "Lahari",
#     "age": 22,
#     "course": "AI/ML",
#     "is_active": True
# }
# access the values
# print(student["name"])
# print(student.get("age"))

# # add/update the values
# student["age"] = 23
# student["city"] = "Hyderabad"

# # remove items
# student.pop("city")
# del student["is_active"]

# print(student)

# for key, value in student.items():
#     print(key, value)


# Conditions
# age = 18

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")

# marks = 85

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")



# age = 22
# is_student = True

# if age > 18 and is_student:
#     print("Student discount applied")


# user = {
#     "username": "lahari",
#     "role": "admin",
#     "active": True
# }

# if user["role"] == "admin" and user["active"]:
#     print("Access granted")
# else:
#     print("Access denied")



"""Task 1
Create a dictionary with:
name
age
marks
👉 Print:
"Pass" if marks ≥ 40
"Fail" otherwise
"""

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "marks": 35
# }

# if student["marks"] >= 40:
#     print("Pass")
# else:
#     print("Fail")

"""Task 2
user = {
    "username": "admin",
    "password": "1234"
}
 Ask user to enter username & password
 If both match → "Login successful"
 Else → "Invalid credentials"""

# user = {
#     "username": "admin",
#     "password": "1234"
# }

# entered_username = input("Enter username: ")
# entered_password = input("Enter password: ")

# if entered_username == user["username"] and entered_password == user["password"]:
#     print("Login successful")
# else:
#     print("Invalid credentials")

"""Task 3
marks = {
    "maths": 78,
    "science": 85,
    "english": 72
}
 Calculate average
 Use conditions to print grade"""

# marks = {
#     "maths": 78,
#     "science": 85,
#     "english": 72
# }

# average = sum(marks.values()) / len(marks)

# print("Average Marks:", average)

# if average >= 90:
#     print("Grade: A+")
# elif average >= 75:
#     print("Grade: A")
# elif average >= 60:
#     print("Grade: B")
# elif average >= 40:
#     print("Grade: C")
# else:
#     print("Grade: F")

"""Task 4
Task 4: Count Word Frequency (⭐ Important)
sentence = "python is easy and python is powerful"
 Output:
{
  "python": 2,
  "is": 2,
  "easy": 1,
  "and": 1,
  "powerful": 1
}
"""

# # Sentence
# sentence = "python is easy and python is powerful"

# # Split sentence into words
# words = sentence.split()

# # Create empty dictionary
# frequency = {}

# # Count word frequency
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# # Print result
# print(frequency)

"""Task 5
profile = {
    "name": "Lahari",
    "age": 22,
    "email_verified": True
}
 Conditions:
If age ≥ 18 AND email verified → "Profile approved"
Else → "Profile incomplete" """

# profile = {
#     "name": "Lahari",
#     "age": 22,
#     "email_verified": True
# }

# if profile["age"] >= 18 and profile["email_verified"] == True:
#     print("Profile approved")
# else:
#     print("Profile incomplete")


"""Task 6
Create a dictionary for one employee with:
name, age, salary, experience
Print each value"""

# employee = {
#     "name": "Ravi",
#     "age": 30,
#     "salary": 50000,
#     "experience": 5
# }

# print("Name:", employee["name"])
# print("Age:", employee["age"])
# print("Salary:", employee["salary"])
# print("Experience:", employee["experience"])

"""Task 7
employee = {
    "name": "Asha",
    "age": 26,
    "salary": 45000
}
# Try accessing "experience"
# Use .get() with default value"""

# employee = {
#     "name": "Asha",
#     "age": 26,
#     "salary": 45000
# }

# experience = employee.get("experience", "Not available")
# print("Experience:", experience)

"""Task 8
metrics = {
    "accuracy": 0.88,
    "precision": 0.85,
    "recall": 0.87
}
# If accuracy >= 0.9 → "Excellent"
# If accuracy >= 0.8 → "Good"
# Else → "Poor"
"""

# metrics = {
#     "accuracy": 0.88,
#     "precision": 0.85,
#     "recall": 0.87
# }

# if metrics["accuracy"] >= 0.9:
#     print("Excellent")
# elif metrics["accuracy"] >= 0.8:
#     print("Good")
# else:
#     print("Poor")

"""Task 9
data = {
    "age": -1,
    "salary": 50000
}
# If age < 0, print "Invalid age"
# Else print "Valid data" """

# data = {
#     "age": -1,
#     "salary": 50000
# }

# if data["age"] < 0:
#     print("Invalid age")
# else:
#     print("Valid data")

"""Task 10
model = {
    "name": "LogisticRegression",
    "accuracy": 0.78
}
# If accuracy < 0.8:
# Add key "retrain" = True
"""

# model = {
#     "name": "LogisticRegression",
#     "accuracy": 0.78
# }

# if model["accuracy"] < 0.8:
#     model["retrain"] = True

# print(model)

"""Task 11
model_results = {
    "LR": 0.82,
    "SVM": 0.89,
    "RF": 0.91
}
# Print models with accuracy >= 0.85"""

# model_results = {
#     "LR": 0.82,
#     "SVM": 0.89,
#     "RF": 0.91
# }

# for model, accuracy in model_results.items():
#     if accuracy >= 0.85:
#         print(model, ":", accuracy)

