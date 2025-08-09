"""
Write a Python function that takes a list of integers and returns the smallest positive integer that does not appear in the list.

input_list = [3, 4, -1, 1]
Expected output: 2

input_list = [1, 2, 0]
Expected output: 3
"""

def smallest_positive_integer(list):
    temp_list = list

    for i in range(len(temp_list) - 1):
        for j in range(i + 1, len(temp_list)):
            if temp_list[i] < temp_list[i + 1]:
                temp = temp_list[i]
                temp_list[i] = temp_list[i + 1]
                temp_list[i + 1] = temp

    for i in range(len(temp_list) - 1):
        if temp_list[i] - 1 != temp_list[i + 1]:
            return temp_list[i] - 1
        
    return temp_list[0] + 1

print(smallest_positive_integer([3, 4, -1, 1]))
print(smallest_positive_integer([1, 2, 0]))