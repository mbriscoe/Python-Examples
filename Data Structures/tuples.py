# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements of a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'a'

# Slicing a tuple
print(my_tuple[2:5])  # Output: (3, 'a', 'b')

# Modifying elements of a tuple (not allowed)
my_tuple[0] = 10  # This will raise an error

# Concatenating tuples
new_tuple = my_tuple + ('x', 'y', 'z')
print(new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 'x', 'y', 'z')

# Tuple unpacking
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)  # Output: 1 2 3 'a' 'b' 'c'

# Length of a tuple
print(len(my_tuple))  # Output: 6

# Checking if an element exists in a tuple
print('a' in my_tuple)  # Output: True
print('x' in my_tuple)  # Output: False
