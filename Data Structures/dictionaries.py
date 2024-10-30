# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# Accessing dictionary values
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 20

# Modifying dictionary values
student["age"] = 21
student["major"] = "Data Science"

# Adding new key-value pairs
student["university"] = "ABC University"

# Removing a key-value pair
del student["major"]

# Iterating over dictionary
for key, value in student.items():
    print(key, ":", value)

# Checking if a key exists in the dictionary
if "name" in student:
    print("Name exists in the dictionary")

# Getting the number of key-value pairs in the dictionary
print("Number of key-value pairs:", len(student))
