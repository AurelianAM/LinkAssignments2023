
# Defined the input string - hardcode
input_string = "3,9,13,4,42"

# transfer parts of the input string divided by coma ','
# into a list used for calculations
calc_list = input_string.split(',')

# convert the list's elements into integers, calculate the power 2
# and convert the result into strings, back to the same list
calc_list = [str(int(element)**2) for element in calc_list]

# join the list's elements into an output string, separated by coma ','
output_string = ','.join(calc_list)

# print the output string - the result
print(output_string)