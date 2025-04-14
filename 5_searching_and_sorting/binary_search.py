
num_list = [1,3,4,5,6,8,9,13,16,17,18,23,25,26,27,39,80,90,100]

def binary_search(ordered_list, searched_number):
    halfway_index = len(ordered_list)//2
    if halfway_index == 0:
        print('number not found')
        return
    elif ordered_list[halfway_index] == searched_number:
        return halfway_index
    elif ordered_list[halfway_index] > searched_number:
        binary_search(ordered_list[:halfway_index], searched_number)
    elif ordered_list[halfway_index] < searched_number:
        binary_search(ordered_list[halfway_index:], searched_number)





print(binary_search(num_list, 6))