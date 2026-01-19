# data types in python int , float , string , boolean , None

# age = 23
# height = 5.3
# Name = "lahari"
# learning = True
# Company = None

# print(type(age))
# print(type(height))
# print(type(Name))
# print(type(learning))
# print(type(Company))


# user_age = "23"

# converted_age = int(user_age)
# print(converted_age, type(converted_age))


""" A List stores multiple values in order"""
""" ML Datasets = Lists --> arrays --> Dataframes"""

# subjects = ["maths", "AI", "ML", "Python"]
# # print(subjects)
# # print(subjects[0])
# # print(subjects[-1])

# for subject in subjects:
#     print(subject)


# numbers = [10, 20, 30]
# numbers.append(40)
# numbers.remove(20)
# numbers.insert(0, 25)
# print(numbers)


"""Task 1"""
# marks = [78, 85, 90, 66, 88]
# 1. Print all marks
# 2. Print highest mark
# 3. Print lowest mark
# 4. Calculate average

marks = [78, 85, 90, 66, 88]
print(marks)
print(max(marks))
print(min(marks))
print(sum(marks))


"""Task 2"""
# skills = ["Python", "SQL"]
# Add: ML, NLP, Deep Learning
# Remove: SQL
# Print final list

skills = ["Python", "SQL"]
# skills.append("ML") 
# skills.append ("NLP") 
# skills.append("Deep Learning")
skills.extend(["ML", "NLP", "Deep Learning"])
skills.remove("SQL")
print(skills)

"""Task 3"""
# data = [10, 2.5, "AI", True, None]
# Print value and its type using loop

data = [10, 2.5, "AI", True, None]
for info in data:
    print(info, type(info))
    