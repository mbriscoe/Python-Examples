def fizz_buzz_short(number):
    return f"{ '' if number % 3 else 'Fizz'}{'' if number % 5 else 'Buzz' }" or number


for i in range(1, 31):
    print(fizz_buzz_short(i))


# LONG WAY ROUND
def fizz_buzz_long(number):
    if not (number % 15):
        print("FizzBuzz")
    elif not (number % 3):
        print("Fizz")
    elif not (number % 5):
        print("Buzz")
    else:
        print(number)


for i in range(1, 31):
    fizz_buzz_long(i)
