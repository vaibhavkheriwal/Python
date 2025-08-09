"""
Write a Python function that takes a list of integers as input and returns the largest difference between any two numbers in the list. Ensure that the function efficiently handles both small and large lists.
"""

def difference_between_any_two_numbers(my_list_clone):
    if len(my_list_clone) < 2:
        print("Your list has not enough numbers.")
        return 0
    else:
        temp = 0
        for i in range(len(my_list_clone)):
            for j in range(i + 1, len(my_list_clone)):
                    if (my_list_clone[i] - my_list_clone[j] > temp):
                        temp = my_list_clone[i] - my_list_clone[j]
        return temp

my_list = [2, 3, 10, 6, 4, 8, 1]
print(difference_between_any_two_numbers(my_list))