"""
Write a Python function that takes a list of integers and returns a new list containing all the integers from the original list that are prime numbers.

input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: [2, 3, 5, 7]
"""

def prime_numbers(number_list):

    k = 0
    output_list = []

    for i in range(len(number_list)):

        if number_list[i] > 1:

            for j in range(1, number_list[i] + 1):

                if number_list[i] % j == 0:
                    k += 1

            if k == 2:
                output_list.append(number_list[i])

            k = 0

    return output_list

print(prime_numbers([2, 3, 4, 5, 6, 7, 8, 9, 10]))