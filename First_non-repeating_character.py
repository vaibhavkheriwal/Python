"""
Write a Python function that finds the first non-repeating character in a given string. If all characters are repeating, return None.

input_string = "swiss"
Expected output: "w"
"""

def check_char(string):
    do_not_find = [] # store char that we do not need to find

    for i in range(len(string)): # loop i

        for j in range(i + 1, (len(string))): # loop j

            if string[i] != string[j] and string[i] not in do_not_find: # check if you do not find same char

                if j == len(string) - 1: # if we can not find that char till last of string
                    return string[i]     # return that char

            elif string[i] == string[j] and string[i] not in do_not_find: # check if you find same char
                do_not_find.append(string[i])                             # append same char in list so that we do not find same char again

    if string[-1] not in do_not_find: # check last element of string if last element is not in list
        return string[-1]             # return that element

    return None

print(check_char("QisabibQsaQn"))