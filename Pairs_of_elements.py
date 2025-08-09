"""
Write a Python function to find all pairs of elements in a given list of integers that sum up to a specified target value.

input_list = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
Expected output: [(2, 5), (4, 3), (-2, 9)]
"""

def pairs_of_elements(num_list, target_sum):
    output_list = []

    for i in range(len(num_list)):

        for j in range(i + 1, len(num_list)):

            if num_list[i] + num_list[j] == target_sum:

                if ((num_list[i], num_list[j]) not in output_list) and ((num_list[j], num_list[i]) not in output_list):
                    output_list.append((num_list[i], num_list[j]))

    return output_list

input_list = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(pairs_of_elements(input_list, 7))