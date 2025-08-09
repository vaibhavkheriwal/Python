"""
Write a Python function to determine if a given string is a palindrome. A palindrome is a string that reads the same backward as forward. The function should ignore spaces, punctuation, and case differences.

input_string = "A man, a plan, a canal, Panama"
Expected output: True

input_string = "Hello, World!"
Expected output: False
"""

# Riya's code

def Palindrome(input_string):
    string_1 = ""
    string_2 = ""
    n = len(input_string) - 1

    for i in range(len(input_string)):

        if(input_string[i].isalpha()):
            string_2 += input_string[i].lower()

        m = n - i

        if(input_string[m].isalpha()):
            string_1 += input_string[m].lower()

    return string_2==string_1

Palindrome("r ,a a...r")