"""
Given an array of strings words and an integer k, return the k most frequent strings. Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input:
words = ["i", "love", "brainmentors", "i", "love", "coding"], k = 2
Output:
["i", "love"]

Example 2:
Input:
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k
= 4
Output:
["the", "is", "sunny", "day"]
"""

def most_frequent_strings(string, k):
    number_of_element_list = []
    number_of_element = 0

    # find the count of each element
    for i in range(len(string)):

        for j in range(len(string)):

            if string[i] == string[j]:
                number_of_element += 1

        if (string[i], number_of_element) not in number_of_element_list:
            number_of_element_list.append((string[i], number_of_element))

        number_of_element = 0
    
    for i in range(len(number_of_element_list) - 1):

        if number_of_element_list[i][1] < number_of_element_list[i + 1][1]:
            temp = number_of_element_list[i]
            number_of_element_list[i] = number_of_element_list[i + 1]
            number_of_element_list[i + 1] = temp

    for i in range(len(number_of_element_list)):
        number_of_element_list[i] = number_of_element_list[i][0]

    return number_of_element_list[0:k]

print(most_frequent_strings(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))