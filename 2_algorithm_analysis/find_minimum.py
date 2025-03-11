
# Self Check

# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. 
# The second function should be linear.
import math
import random
import time
# 0(n)
def find_min(list):
    start = time.time()
    current_min = math.inf
    for i in range(len(list)):
        current_num = list[i]
        if current_num < current_min:
            current_min = current_num
    end = time.time()
    return current_min, end - start

# O(nˆ2)
def find_min_dumb(list):
    start = time.time()
    for i in range(len(list)):
        current_num = list[i]
        lower_numbers = []
        for j in range(len(list)):
            if current_num > list[j]:
                lower_numbers.append(list[j])
        if not lower_numbers:
            end = time.time()
            return current_num, end - start
        

random_list = [random.randint(1, 100) for _ in range(1000000)]
# print(random_list)
print(find_min(random_list))
print(find_min_dumb(random_list))

