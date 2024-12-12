# Standard Way
def odd_numbers_only_standard(numbers):
    arr = []
    for num in numbers:
        if num % 2 != 0:
            arr.append(num)
    return arr


# Using List Comprehension
def odd_numbers_only(numbers):

    return [num for num in numbers if num % 2]


number_list = [12, 45, 60, 87, 999, 200, 85, 77, 2, 3]

res = odd_numbers_only(number_list)

print(res)

newlist = [x for x in number_list]
print(newlist)
