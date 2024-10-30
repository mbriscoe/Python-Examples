# *args
# In this example, the `sum_numbers` function accepts any number of arguments and calculates their sum using a loop.
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(10, 20, 30, 40))  # Output: 100


# **kwargs
# In this example, the `print_info` function accepts any number of keyword arguments and prints them out. The keyword arguments are passed as key-value pairs, and within the function, they are accessible as a dictionary.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="John", age=25, city="New York")

# You can also use both `args` and `kwargs` in the same function definition if you want to handle both positional and keyword arguments.
