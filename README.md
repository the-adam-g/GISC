GISC (pronounced “Jee-ISC”) is a custom 16-bit Instruction Set Architecture designed and implemented by Adam Gillion. It features a hybrid RISC/CISC-inspired design and has been built both as a software interpreter and as a hardware CPU using Logisim Evolution.

Features:
- 16-bit instruction format
- 5 general-purpose registers (including accumulator)
- 256 bytes of memory
- Fully working hardware CPU (Logisim)
- Software interpreter (Python)
- Rich control flow:
- - JMP, JZ, JP, JN
- - COM (compare + branch)
- - GOTO (counted loop instruction)

Instruction format:
All instructions are 16 bits:
[ OPCODE (4 bits) ][ ARG1 (4 bits) ][ ARG2 (8 bits) ]

Instruction set + examples:

1 - Load [opcode][register][literal value (2 hexadecimals)]
2 - ADD [opcode][emptyspace][register1][register2]
3 - SUB [opcode][emptyspace][minuend][subtrahend]
4 - MOV [opcode][emptyspace][destination][source]
5 - LOADM [opcode][emptyspace][memoryaddr][registersource]
6 - JMP [opcode][emptyspace][address(2 bytes)]
7 - JZ [opcode][register][address(2 bytes)]
8 - JP [opcode][register][address(2 bytes)]
9 - JN [opcode][register][address(2 bytes)]
10 - COM [opcode][address][register1][register2]
11 - GOTO [opcode][address (2 bytes)][times to loop]
12 - SAVEM [opcode][emptyspace][destinationregister][sourcememoryaddr]
13 - HLT [opcode][emptyspace (3 bytes)]

Example usage:
1309 - Load the value 9 into register 3
2001 - Add together the contents of register 0 (ACC) and register 1
3021 - Subtract the contents of register 1 from register 2
4040 - Move the contents of register 0 (ACC) to register 4
502c - Copy the contents of memory address 12 to register 2
6050 - Jump to ROM address 
7360 - If register 3 == 0, jump to line 60 (hexadecimal, literal is 96)
8370 - If register 3 is positive, jump to line 70
9380 - If register 3 is negative, jump to line 80
af32 - If register 3 = register 2 goto line 15 (f)
b2a4 - GOTO line 2a, 4 times
c0c3 - Save the contents of register 3 to memory address 12
d*** - Halt all processes
*** = any number can go here
