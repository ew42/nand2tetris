from parser import Parser
from code import *

def assemble(filePath):
    '''
    filePath comes in
    symbolTable = {}
    with open(binFile.hack, 'w') as file:
        firstRun = Parser(filePath)
            while firstRun.hasMoreLines:
                firstRun.advance()
                if firstRun.instructionType() == lInstruct:
                    firstRun.symbol(
        secondRun = Parser(filePath)
            while secondRun.hasMoreLines:
                secondRun.advance()
                kindOfInstruction = secondRun.instructionType()
                if aInstuct:
                    if secondRun.symbol()[0] == '0'/'1':
                        file.write(0 + secondRun.symbol()):
                    else:
                        file.write(0 + symbolTable[secondRun.symbol()]
    '''
    symbolTable = {}
    for x in range(16):
        symbolTable['R'+str(x)] = x

    symbolIncrement = 16
    with open('binFile.txt', 'w') as file: #replace binFile.hack
        firstRun = Parser(filePath)
        while firstRun.hasMoreLines():
            firstRun.advance()
            if firstRun.instructionType() == 'L_INSTRUCTION':
                symbolTable[firstRun.symbol()] = symbolIncrement
                symbolIncrement += 1
        print(symbolTable)
        secondRun = Parser(filePath)
        while secondRun.hasMoreLines():
            secondRun.advance()
            kindOfInstruction = secondRun.instructionType()
            if kindOfInstruction == 'A_INSTRUCTION':
                instruction = secondRun.symbol()
                if instruction[0].isdigit():
                    file.write('0' + format(int(instruction), '015b') + '\n')
                if instruction in symbolTable:
                    file.write('0' + format(symbolTable[instruction], '015b') + '\n')
            elif kindOfInstruction == 'C_INSTRUCTION':
                cInstruct = ['111']
                cInstruct.append(comparison(secondRun.comp()))
                cInstruct.append(destination(secondRun.dest()))
                # print(destination(secondRun.dest()))
                # print(comparison(secondRun.comp()))
                cInstruct.append(jumper(secondRun.jump()))
                # print(jumper(secondRun.jump()))
                file.write(''.join(cInstruct) + '\n')

if __name__ == '__main__':
    fyle = 'max/Max.asm'
    assemble(fyle)

