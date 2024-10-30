# Create a set
my_set = {1, 2, 3, 4, 5}

# Print the set
print(my_set)

# Add an element to the set
my_set.add(6)

# Remove an element from the set
my_set.remove(3)

# Check if an element is present in the set
print(2 in my_set)

# Iterate over the set
for element in my_set:
    print(element)

# Get the length of the set
print(len(my_set))

# Perform set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1.union(set2)
print(union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)

# Difference of two sets
difference_set = set1.difference(set2)
print(difference_set)
