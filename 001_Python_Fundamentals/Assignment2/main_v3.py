def split_line(string):
    global operations

    for op in operations:
        if op in string:
            result = string.split(op)
            result = [int(el) for el in result]
            result.insert(1,op)
            result.append('=')
            return result
        else:
            for i in range(len(string)):
                if string[i].isnumeric():
                    continue
                else:
                    x = string[i]
                    result = string.split(x)
                    result = [int(el) for el in result]
                    result.insert(1,x)
                    result.append('=')
                    return result


def calculation(lst):
    global operations
    try:
        if lst[1] == operations[0]:
            lst.append(lst[0] + lst[2])
        elif lst[1] == operations[1]:
            lst.append(lst[0] - lst[2])
        elif lst[1] == operations[2]:
            lst.append(lst[0] * lst[2])
        elif lst[1] == operations[3]:
            if lst[2]:
                lst.append(lst[0] / lst[2])
            else:
                lst.append('Div by 0 error')
        else:
            lst.append('Unknown operator')
        lst = [str(el) for el in lst]
    except TypeError:
        pass
    return lst


operations = ['+', '-', '*', '/']

try:
    f = open('./expresii.txt')
    f_out = open('./iesire.txt', 'w')
    endoffile = False
    while endoffile == False:
        line = f.readline()
        if '\n' in line:
            line = line[0:len(line)-1]
            calc_list = split_line(line)
            calc_list = calculation(calc_list)
            line = ''.join(calc_list)
            f_out.write(line+'\n')

        else:
            calc_list = split_line(line)
            calc_list = calculation(calc_list)
            line = ''.join(calc_list)
            f_out.write(line)
            endoffile = True

finally:
    f.close()
    f_out.close()

