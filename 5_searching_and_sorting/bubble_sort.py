num_list = [288, 5, 12, 15, 38, 22, 2, 2, 88, 1003]

def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
    return a_list


print(bubble_sort(num_list))