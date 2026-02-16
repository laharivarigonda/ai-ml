"""Task 1
Print numbers from 1 to 20.
Print even numbers from 1 to 50.
Print sum of numbers from 1 to 100.
Print each character of your name.
Count how many numbers in a list are greater than 10."""

# for i in range(1, 21):
#     print(i)

# for i in range(2, 50, 2):
#     print(i)

# total = sum(range(1, 101))
# print(total)

# name = "shiva"
# for char in name:
#     print(char)

# numbers = [3, 7, 12, 18, 5, 25, 9]
# count = sum(1 for num in numbers if num > 10)
# print(count)


"""Task 2
Reverse a string using a loop.
Count vowels in a string.
Find largest number in a list without using max().
Print multiplication table of a number.
Create a program that keeps asking user input until they type "exit"."""

# text = "hello"
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print(reversed_text)


# text = " AI opens a path for other new technologies, new devices, and new Opportunities"
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print(count)


# numbers = [2, 13, 9, 54, 14, 23, 16]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)


# num = 200
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# while True:
#     user_input = input("Enter something (type 'exit' to quit): ")
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
#     else:
#         print(f"You typed: {user_input}")

"""Task 3
Check if a number is prime.
Print Fibonacci series up to n terms.
Remove duplicates from a list using loops only (no set)."""

# num = 24
# is_prime = True

# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

# n = 10
# a, b = 0, 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b


# numbers = [4, 7, 4, 2, 7, 9, 2, 10]
# unique_list = []

# for num in numbers:
#     if num not in unique_list:
#         unique_list.append(num)

# print(unique_list)

"""Task 4
Build a small CLI program:
👉 Employee Salary Calculator
Store employee names in list
Ask user for salary
If salary > 50,000 → print "High earner"
Else → "Normal earner"
Continue until user stops"""

# employees = []

# while True:
#     name = input("Enter employee name (or type 'stop' to finish): ")
#     if name.lower() == "stop":
#         break
    
#     employees.append(name)
#     salary = float(input(f"Enter salary for {name}: "))
    
#     if salary > 50000:
#         print("High earner")
#     else:
#         print("Normal earner")

# print("\nEmployee list:")
# for emp in employees:
#     print(emp)


"""Task 5
scores = [78, 85, 90, 67, 88]
# Print:
# "Score: X"
"""
# scores = [78, 85, 90, 67, 88]

# for score in scores:
#     print(f"Score: {score}")

"""Task 6
scores = [45, 76, 89, 34, 90]
# Count how many scores >= 60
"""
# scores = [45, 76, 89, 34, 90]

# count = 0
# for score in scores:
#     if score >= 60:
#         count += 1

# print("Number of scores >= 60:", count)

"""Task 7
model_results = {
    "LR": 0.82,
    "SVM": 0.89,
    "RF": 0.91,
    "KNN": 0.75
}
# Print models with accuracy >= 0.85
"""

# model_results = {
#     "LR": 0.82,
#     "SVM": 0.89,
#     "RF": 0.91,
#     "KNN": 0.75
# }
# for model, accuracy in model_results.items():
#     if accuracy >= 0.85:
#         print(f"{model}: {accuracy}")

"""Task 8
model_results = {
    "LR": 0.82,
    "SVM": 0.89,
    "RF": 0.91
}
# Find average accuracy
"""
# model_results = {
#     "LR": 0.82,
#     "SVM": 0.89,
#     "RF": 0.91
# }

# total = 0
# count = 0
# for accuracy in model_results.values():
#     total += accuracy
#     count += 1
# average = total / count
# print("Average accuracy:", average)

"""Task 9
text = "AI is transforming the world"
# Print each word on new line
"""
# text = "AI is transforming the world"

# for word in text.split():
#     print(word)


"""Task 10
Simulate Model Training (while loop)

accuracy = 0.5
# Increase accuracy by 0.1
# Until it reaches 0.9
# Print each step"""

# accuracy = 0.5

# # Simulate training loop
# while accuracy < 0.9:
#     print(f"Current accuracy: {accuracy:.1f}")
#     accuracy += 0.1

# # Final step
# print(f"Final accuracy: {accuracy:.1f}")

"""Task 11
Feature Validation System (Advanced)
data = {
    "age": 25,
    "salary": -50000,
    "experience": 3
}
# Loop through dictionary
# If any value < 0:
# Print "Invalid feature: key" """

# data = {
#     "age": 25,
#     "salary": -50000,
#     "experience": 3
# }
# # Loop through dictionary
# for key, value in data.items():
#     if value < 0:
#         print(f"Invalid feature: {key}")

"""Task 12
models = {
    "LR": 0.82,
    "SVM": 0.89,
    "RF": 0.91,
    "XGBoost": 0.94
}
# Find the best model using loop
# Print:
# Best model: X with accuracy Y
No built-in max() shortcut. Use logic."""

# models = {
#     "LR": 0.82,
#     "SVM": 0.89,
#     "RF": 0.91,
#     "XGBoost": 0.94
# }

# best_model = None
# best_accuracy = 0.0

# # Loop through dictionary
# for key, value in models.items():
#     if value > best_accuracy:
#         best_accuracy = value
#         best_model = key

# print(f"Best model: {best_model} with accuracy {best_accuracy}")

