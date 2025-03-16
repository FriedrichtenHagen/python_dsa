from collections import deque

def base_converter(num, base):
    if num == 0:
        return '0'
    
    stack = deque()
    # take number and divide by base
    while num > 0:
        current_modulo = num % base
        stack.append(current_modulo)
        # overwrite num with result of floor division
        current_floor_division = num // base
        num = current_floor_division
        # print(current_modulo)
    # read out stack into a string
    result = ''.join(str(stack.pop()) for _ in range(len(stack)))
    return result

        
assert base_converter(11, 2) == "1011"   # Binary to Decimal
assert base_converter(10, 8) == "12"  # 10 in octal is 12
assert base_converter(0, 2) == "0"  # Edge case
print('all tests passed')

print(base_converter(11, 2))