def rev_string(my_str):
    my_stack = []
    # add to stack
    for i in range(len(my_str)):
        my_stack.append(my_str[i])
    # remove from stack
    return_string = ''
    for j in range(len(my_stack)):
        return_string += my_stack.pop()
    return return_string



print(rev_string('Friedrich'))