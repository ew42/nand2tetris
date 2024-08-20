class Parser:
    def __init__(self, filePath):
        self.currentInstruction = -1
        self.lines = []
        with open(filePath, 'r') as file:
            for line in file:
                self.lines.append(line[0:-1].strip())

    def hasMoreLines(self):
        if len(self.lines) - 1 > self.currentInstruction:
            return True
        else:
            return False

    def advance(self):
        if self.hasMoreLines():
            self.currentInstruction += 1
            self.currentLine = self.lines[self.currentInstruction]
            if '//' in self.currentLine or len(self.currentLine) == 0:
                self.advance()

    def instructionType(self):
        instruction = self.lines[self.currentInstruction]
        if instruction[0] == '@':
            return 'A_INSTRUCTION'
        if instruction[0] == '(':
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'

    def symbol(self):
        print(self.instructionType())
        if self.instructionType() == 'A_INSTRUCTION':
            return self.currentLine.strip('@')
        if self.instructionType() == 'L_INSTRUCTION':
            return self.currentLine.strip('()')

    def dest(self):
        if self.instructionType() == 'C_INSTRUCTION':
            if '=' in self.currentLine:
                # print('dest slice', self.currentLine[0: self.currentLine.index('=')])
                return self.currentLine[0: self.currentLine.index('=')]

    def comp(self):
        if self.instructionType() == 'C_INSTRUCTION':
            start = 0
            stop = len(self.currentLine)
            if '=' in self.currentLine:
                start = self.currentLine.index('=') + 1
            if ';' in self.currentLine:
                stop = self.currentLine.index(';')
            # print('Comp slice', self.currentLine[start: stop])
            return self.currentLine[start: stop]

    def jump(self):
        if self.instructionType() == 'C_INSTRUCTION':
            if ';' in self.currentLine:
                # print('jump slice', self.currentLine[self.currentLine.index(';'): len(self.currentLine) - 1])
                return self.currentLine[self.currentLine.index(';'): len(self.currentLine) - 1]

if __name__ == '__main__':
    parsuh = Parser('test.txt')
    parsuh.advance()
    print(parsuh.instructionType())
    parsuh.advance()
    print(parsuh.instructionType())
    parsuh.advance()
    print(parsuh.instructionType())


