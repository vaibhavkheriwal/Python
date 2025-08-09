"""
Write a Python function to determine if a given string is a palindrome. A palindrome is a string that reads the same backward as forward. The function should ignore spaces, punctuation, and case differences.

input_string = "A man, a plan, a canal, Panama"
Expected output: True

input_string = "Hello, World!"
Expected output: False
"""

import re # import re module

def palindrome_string(string):                        # create a function
    temp_string = re.sub(r'[^a-zA-Z0-9]', '', string) # remove all punctuation and spaces by using re.sub()
    temp_string = temp_string.lower()                 # convert all char to lower case

    for i in range(len(temp_string)): # loop to check all char

        if temp_string[i] != temp_string[(len(temp_string) - 1) - i]: # check if char is not equal to char in reverse order
            return False

    return True

palindrome_string("raajk")