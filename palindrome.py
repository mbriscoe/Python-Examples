# QUICK WAY
def isPalindrome(str):
    return str == str[::-1]


# Driver code
test_word = "racecar"
ans = isPalindrome(test_word)

print(
    f"The string {test_word} is a palindrome."
    if ans
    else "The string is not a palindrome."
)
# if ans:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# LONG WAY
def isPalindrome(str):
    revstr = ""

    for i in str:
        revstr = i + revstr
    return str == revstr


# Driver code
test_word = "racecar"
ans = isPalindrome(test_word)

if ans:
    print(f"The string {test_word} is a palindrome.")
else:
    print(f"The string {test_word} is not a palindrome.")
