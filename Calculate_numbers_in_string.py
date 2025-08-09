"""
Write a Python function that takes a string containing an arithmetic expression (only addition and subtraction, no parentheses) and evaluates the expression. Assume the string contains only digits, +, and - symbols, with no spaces. For example: evaluate_expression("10+5-3+8-2")
"""

def calculate_numbers_in_string(number_string): # create a function
    last_symbol_index = 0                       # to check index of last symbol
    list_number = []                            # get all sub string of numbers
    list_symbol = []                            # get all symbol
    calculation_of_numbers = 0

    for i in range(len(number_string)): # loop to insert all sub string in list_number and all symbol in list_symbol

        if "+" == number_string[i] or "-" == number_string[i]: # check if symbol is + or - on i position

            if last_symbol_index == 0:                 # it is run only for first time
                list_number.append(number_string[0:i]) # append first number string in list_number
                list_symbol.append(number_string[i])   # append first symbol in list_symbol
                last_symbol_index = i                  # last_symbol_index is the first symbol index

            else:                                                          # it is not going to run for first and last
                list_number.append(number_string[last_symbol_index + 1:i]) # append number string in list_number using last_symbol_index
                list_symbol.append(number_string[i])                       # append symbol in list_symbol
                last_symbol_index = i                                      # last_symbol_index is the symbol index

    list_number.append(number_string[last_symbol_index + 1:len(number_string)]) # append last number string in list_number using last_symbol_index
    calculation_of_numbers = int(list_number[0])                                # calculation_of_numbers is list_number[0] as a number not string

    for i in range(len(list_symbol)): # loop to calculate numbers

        if "+" == list_symbol[i]:                                                     # check if symbol is +
            calculation_of_numbers = calculation_of_numbers + int(list_number[i + 1]) # calculate numbers

        else:                                                                         # check if symbol is -
            calculation_of_numbers = calculation_of_numbers - int(list_number[i + 1]) # calculate numbers

    print("Input string: ")
    print(number_string)
    print("\nAll numbers: ")
    print(list_number)
    print("\nAll symbols: ")
    print(list_symbol)
    print("\nCalculation of numbers: ")
    print(calculation_of_numbers)

calculate_numbers_in_string("3+5+7-9+0+2")