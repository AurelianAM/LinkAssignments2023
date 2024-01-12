## With this version we are able to solve expresions with multiple operators
## If new operator is added to the operators, if the new operator is two charachters long,
## it will have to be added to the top of the list of operators
## example: OPERATORS = ['**', '+', '-', '*', '/']

OPERATORS = ['+', '-', '*', '/']

def solve_my_expresion(operand_list, operator):
    if operator == OPERATORS[0]:
        result = int(operand_list[0]) + int(operand_list[1])
    elif operator == OPERATORS[1]:
        result = int(operand_list[0]) - int(operand_list[1])
    elif operator == OPERATORS[2]:
        result = int(operand_list[0]) * int(operand_list[1])
    elif operator == OPERATORS[3]:
        if operand_list[1] == '0':
            result = 'Div by 0 error'
        else:
            result = int(operand_list[0]) / int(operand_list[1])
    else:
        result = 'Unknown operator'
    return f'{operand_list[0]}{operator}{operand_list[1]}={result}'


if __name__ == "__main__":
    result_list = []
    with open("./expresii.txt") as f_in:
        expresion_list = f_in.read().split()

    for expresion in expresion_list:
        for operator in OPERATORS:
            if operator in expresion:
                operand_list = expresion.split(operator)
                result_list.append(solve_my_expresion(operand_list, operator))

    with open("./iesire.txt", "w") as f_out:
        for result in result_list:
            f_out.write(result + '\n')
