# This problem is called the string edit distance problem, and is quite useful in many areas of research. 
# Suppose that you want to transform the word algorithm into the word alligator. 
# For each letter you can either copy the letter from one word to another at a cost of 5, 
# you can delete a letter at cost of 20, or insert a letter at a cost of 20. 
# The total cost to transform one word into another is used by spell-check programs to provide suggestions
#  for words that are close to one another. Use dynamic programming techniques to develop an algorithm 
# that gives you the smallest edit distance between any two words.

# Costs for operations
characters_are_same = 0
replace_letter = 5
delete = 20
insert = 20

# Strings to compare
string1 = 'algorithm'
string2 = 'alligator'

def calc_levenstein_distance(string1, string2):
    # Lengths of the strings
    len1 = len(string1)
    len2 = len(string2)

    # Create a DP table with dimensions (len1+1) x (len2+1)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Initialize the base cases
    for i in range(len1 + 1):
        dp[i][0] = i * delete  # Cost of deleting all characters from string1
    for j in range(len2 + 1):
        dp[0][j] = j * insert  # Cost of inserting all characters into string1

    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # If characters are the same, no cost to copy
            if string1[i - 1] == string2[j - 1]:
                cost_replace = dp[i - 1][j - 1] + characters_are_same
            else:
                # If characters are different, cost to replace
                cost_replace = dp[i - 1][j - 1] + replace_letter

            # Calculate the minimum cost for the current cell
            dp[i][j] = min(
                cost_replace,                # Replace
                dp[i - 1][j] + delete,       # Delete
                dp[i][j - 1] + insert        # Insert
            )

    # The final cell contains the minimum cost to transform string1 into string2
    for i in range(len(dp)):
        print(dp[i])
    return dp[len1][len2]

# Calculate and print the result
min_cost = calc_levenstein_distance(string1, string2)
print(f"The minimum cost to transform '{string1}' into '{string2}' is: {min_cost}")
    
    


    
calc_levenstein_distance(string1=string1, string2=string2)
        