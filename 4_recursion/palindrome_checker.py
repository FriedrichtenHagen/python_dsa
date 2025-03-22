def palindrome_checker(input_str):
    return input_str == input_str[::-1]



print(palindrome_checker('kayak'))
print(palindrome_checker('friedrich'))


def palindrome_checker(input_str):
    # Base case: if the string has 0 or 1 character, it's a palindrome
    if len(input_str) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    # and recursively check the substring excluding the first and last characters
    if input_str[0] == input_str[-1]:
        return palindrome_checker(input_str[1:-1])
    # If the first and last characters don't match, it's not a palindrome
    return False