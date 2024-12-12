import os

# Clear the screen
os.system('clear')

# Create an empty list
my_list = []

# Add elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Access elements in the list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2

# Update elements in the list
my_list[2] = 4
print(my_list)  # Output: [1, 2, 4]

# Remove elements from the list
my_list.remove(2)
print(my_list)  # Output: [1, 4]

# Check if an element exists in the list
if 1 in my_list:
    print("1 is in the list")  # Output: 1 is in the list

# Get the length of the list
print(len(my_list))  # Output: 2

# Iterate over the elements in the list
for item in my_list:
    print(item)  # Output: 1, 4
