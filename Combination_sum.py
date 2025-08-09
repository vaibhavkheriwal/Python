"""
Write a Python function that takes an integer n and returns a list of all the unique combinations of k numbers that add up to n. Each number in the combination must be between 1 and 9 (inclusive), and each combination must be sorted in non-descending order. The solution set must not contain duplicate combinations.

n = 7
k = 3
Expected output: [[1, 2, 4]]
"""

def combination_sum(n, k):
    output_list = []
    output_list_sum = 0

    for i in range(1, k):
        output_list.append(i)
        output_list_sum += i
    
    for i in range(k, 10):
        if output_list_sum + i == n:
            output_list.append(i)
            output_list_sum += i
            break

    if len(output_list) != k:
        return None
    
    return output_list

print(combination_sum(8, 4))