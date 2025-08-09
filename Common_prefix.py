"""
Write a Python function that returns the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.

input_strings = ["flower", "flow", "flight"]
Expected output: "fl"
"""

def common_prefix(array_of_string): # create a function
    prefix = ""                     # create a variable to store prefix

    for i in range(len(array_of_string[0])): # loop to check all char of first string
        prefix = array_of_string[0][0:i + 1] # append first char in prefix

        for j in range(len(array_of_string)): # loop to check all string

            if prefix != array_of_string[j][0:i + 1]: # check if prefix is not equal to string
                return prefix[0:i]                    # return prefix

    return prefix # return prefix

common_prefix(["flower", "flow", "floight"])