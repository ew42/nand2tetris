// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

    @i
    M=0
    @j
    M=0
(LOOP)
    @j
    M=0
//if M[KBD] != 0, black
    @KBD 
    D=M
    @BLACK
    D;JGT
    @i
    M=M+1
//if i>1000, white
    @i
    D=M
    @10000
    D=D-A
    @WHITE
    D;JGE
    @LOOP
    0;JMP
//Black out screen
(BLACK)
    @i
    M=0
    @j
    D=M
    @SCREEN
    A=D+A
    M=-1
    @j
    M=M+1
    D=M
    @8192
    D=D-A
    @BLACK
    D;JLE
    @j
    M=0
    @LOOP
    0;JMP
(WHITE)
//white out screen
    @i
    M=0
    @j
    D=M
    @SCREEN
    A=D+A
    M=0
    @j
    M=M+1
    D=M
    @8192
    D=D-A
    @WHITE
    D;JLE
    @j
    M=0
    @LOOP
    0;JMP