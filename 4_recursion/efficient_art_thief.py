# Suppose you are a computer scientist/art thief who has broken into a major art gallery. 
# All you have with you to haul out your stolen art is your knapsack which only holds 
# pounds of art, but for every piece of art you know its value and its weight. 
# Write a dynamic programming function to help you maximize your profit. 
# 
# Here is a sample problem for you to get started: suppose your knapsack can hold a total weight of 20 pounds. You have 5 items as follows:

# item     weight      value
#   1        2           3
#   2        3           4
#   3        4           8
#   4        5           8
#   5        9          10


max_weight = 20

# item weights and values are ordered in the same way
item_weights = [2, 3, 4, 5, 9]
item_values = [3, 4, 8, 8, 10]

def calculate_optimal_item_selection(max_weight, item_weights, item_values):
    for w in range(max_weight + 1):
        if w 
        pass
