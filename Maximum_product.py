"""
Write a Python function that takes a list of integers and returns the maximum product that can be obtained from any three integers in the list.

input_list = [1, 10, 2, 6, 5, 3]
Expected output: 300 (product of 10, 6, and 5)
"""

def maximum_product(input_list, k):

    for i in range(len(input_list) - 1):

        for j in range(i + 1, len(input_list)):

            if input_list[i] < input_list[j]:

                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp

    product = 1

    for i in range(k):

        product = product * input_list[i]

    return product

print(maximum_product([1, 10, 2, 6, 5, 3], 3))