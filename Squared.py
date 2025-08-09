"""
Write a Python function that takes a list of integers and returns a new list with each integer squared.

input_list = [1, 2, 3, 4, 5]
Expected output: [1, 4, 9, 16, 25]
"""

def squared(list_1):
    list_2 = []

    for i in range(len(list_1)):
        list_2.append(list_1[i] * list_1[i])

    return list_2

print(squared([1, 2, 3, 4, 5]))