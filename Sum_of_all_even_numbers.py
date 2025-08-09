"""
Write a Python function that takes a list of integers and returns the sum of all even numbers in the list.

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: 30 (2 + 4 + 6 + 8 + 10)
"""

def  sum_of_all_even_numbers(num_list):
    sum = 0

    for i in num_list:

        if i % 2 == 0:
            sum = sum + i

    return sum

print(sum_of_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))