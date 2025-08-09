"""
Write a Python function that takes a list of strings and returns a new list with the lengths of each string.

input_strings = ["apple", "banana", "cherry", "date"]
Expected output: [5, 6, 6, 4]
"""

def lengths_of_each_string(list_1):
    list_2 = []

    for i in range(len(list_1)):
        list_2.append(len(list_1[i]))

    return list_2

print(lengths_of_each_string(["apple", "banana", "cherry", "date"]))