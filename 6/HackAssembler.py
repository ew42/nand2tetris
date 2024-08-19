"""
HackAssembler.py
Takes HackAssembly and converts into binary instructions
for the Hack CPU

Okay so it needs to loop
    - read line
    - if line //
        next loop
    - if line @
        convert into a-instruct
        write into xxx.hack
    - if line has a first digit != '@'
        convert into b-instruct
        write into xxx.hack
"""

import argparse
import re

def aInstruct(decimalNum):
    fBin = [0]*15
    bin = [1]
    for x in range(1,15):
        bin.insert(0, 2**x)

    for pos in range(len(fBin)):
        if bin[pos] > decimalNum:
            continue
        elif bin[pos] == decimalNum:
            fBin[pos] = 1
            break
        elif bin[pos] < decimalNum:
            fBin[pos] = 1
            decimalNum -= bin[pos]
            continue
    return fBin

def main():
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    parser = argparse.ArgumentParser(description="Process a file.")
    parser.add_argument('filename', type=str, help="The file to be processed")


    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        for lines in file:
            lines = lines.replace(' ', '')
            if lines[0] == '':
                continue
            elif lines[0:2] == "//":
                continue
            elif lines[0] == "@":
                # convert into binary a-instruct
                address = int(lines[1:])

                # write to conversion file
            else:
                lines = 
                # convert into binary c-instruct
                # write to conversion file


    

if __name__ == "__main__":
    # main()
    # print(aInstruct(0))
    print(aInstruct(31))
    print(aInstruct(1025))

