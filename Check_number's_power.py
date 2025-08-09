input_base_number = int(input("Enter a base number: "))
input_power_number = int(input("Enter a power number: "))

def check_power(constant_value_base_number, value_base_number, value_power_number):
  if(constant_value_base_number * value_base_number == value_power_number):
    print("True")
    return 0
  elif(value_base_number > value_power_number):
    print("False")
    return 0
  else:
    value_base_number = value_base_number * constant_value_base_number
    check_power(constant_value_base_number, value_base_number, value_power_number)

check_power(input_base_number, input_base_number, input_power_number)