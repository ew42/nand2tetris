def destination(symbolic):
    binary = []
    if symbolic == 'null':
        return '000'
    if symbolic == None:
        return '000'
    if "A" in symbolic:
        binary.append('1')
    else:
        binary.append('0')
    if "D" in symbolic:
        binary.append('1')
    else:
        binary.append('0')
    if "M" in symbolic:
        binary.append('1')
    else:
        binary.append('0')
    return ''.join(binary)

def comparison(symbolic):
    binary = []
    if 'M' in symbolic:
        binary.append('1')

    else:
        binary.append('0')

    if '&' in symbolic:
        binary.append('0'*6)

    elif '|' in symbolic:
        binary.append('010101')

    elif symbolic == '0':
        binary.append('101010')

    elif symbolic == '1':
        binary.append('111111')

    elif symbolic == '-1':
        binary.append('111010')

    elif symbolic == 'D':
        binary.append('001100')

    elif symbolic == 'A' or symbolic == 'M':
        binary.append('110000')

    elif symbolic == '!D':
        binary.append('001101')

    elif symbolic == '!A' or symbolic == '!M':
        binary.append('110001')

    elif symbolic == '-D':
        binary.append('001111')

    elif symbolic == '-A' or symbolic == '-M':
        binary.append('110011')

    elif symbolic == 'D+1':
        binary.append('011111')

    elif symbolic == 'A+1' or symbolic == 'M+1':
        binary.append('110111')

    elif symbolic == 'D-1':
        binary.append('001110')

    elif symbolic == 'A-1' or symbolic == 'M-1':
        binary.append('110010')

    elif symbolic == 'D+A' or symbolic == 'D+M':
        binary.append('000010')

    elif symbolic == 'D-A' or symbolic == 'D-M':
        binary.append('010011')

    elif symbolic == 'A-D' or symbolic == 'M-D':
        binary.append('000111')

    return "".join(binary)

def jumper(symbolic):
    if symbolic == 'JMP':
        return '111'

    elif symbolic == 'JGT':
        return '001'

    elif symbolic  == 'JEQ':
        return '010'

    elif symbolic == 'JGE':
        return '011'

    elif symbolic == 'JLT':
        return '100'

    elif symbolic == 'JNE':
        return '101'

    elif symbolic == 'JLE':
        return '110'

    else:
        return '000'




if __name__ == '__main__':
    pass
















































