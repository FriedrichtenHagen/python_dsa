from collections import deque





def tower_of_hanoi(number_of_plates):
    stack1 = deque()
    stack2 = deque()
    stack3 = deque()
    # populate the inital stack
    for i in range(number_of_plates):
        stack1.append(number_of_plates - i)

    # move stack1 to stack3
    


tower_of_hanoi(5)