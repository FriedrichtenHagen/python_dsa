def string_reverser(input_string):
    # Base case: if the string is empty or has one character, return it
    if len(input_string) <= 1:
        return input_string
    # Recursive case: reverse the rest of the string and append the first character
    return string_reverser(input_string[1:]) + input_string[0]

# Test the function
print(string_reverser('test'))  # Output: 'tset'