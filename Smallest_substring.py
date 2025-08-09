"""
Write a Python function that finds the smallest window (substring) in a given string s that contains all the characters of another string t. If no such window exists, return an empty string. If there are multiple windows with the same length, return the one that appears first.

s = "ADOBECODEBANC"
t = "ABC"
Expected output: "BANC"
"""

def smallest_substring(string, t):
    substring_start_index = 0
    substring_end_index = 0
    n = 0
    substring_list = []
    do_not_find_char = []
    have_start = False

    for i in range(len(string)):

        for j in range(i, len(string)):

            for k in range(len(t)):

                if string[j] == t[k] and string[j] not in do_not_find_char:

                    if have_start == False:
                        substring_start_index = j
                        have_start = True

                    n += 1
                    substring_end_index = j
                    do_not_find_char.append(string[j])
                    break

            if n == len(t):
                break

        if n == len(t) and string[substring_start_index: substring_end_index + 1] not in substring_list:
            substring_list.append(string[substring_start_index: substring_end_index + 1])

        n = 0
        have_start = False
        do_not_find_char = []

    for i in range(len(substring_list) - 1):

        for j in range(i + 1, len(substring_list)):

            if len(substring_list[i]) > len(substring_list[j]):
                temp = substring_list[i]
                substring_list[i] = substring_list[j]
                substring_list[j] = temp

    return substring_list[0]

print(smallest_substring("ADOBECODEBANC", "ABC"))