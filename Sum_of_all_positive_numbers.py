"""
Implement the sum_positive_numbers function as a recursive function that returns the sum of all positive numbers between the number n received and 1. 

Example:
when n is 3 it should return 1+2+3=6,
and when n is 5 it should return 1+2+3+4+5=15.
"""

input_number = int(input("Enter a number: "))

def sum_positive_numbers(input_number, input_number_):
    if input_number_ > 0:
        return sum_positive_numbers(input_number + (input_number_ - 1), input_number_ - 1)
    else:
        return input_number

print(sum_positive_numbers(input_number, input_number))