<h1>Overview</h1>
GISC (pronounced “Jee-ISC”) is a custom 16-bit Instruction Set Architecture designed and implemented by Adam Gillion. It features a hybrid RISC/CISC-inspired design and has been built both as a software interpreter and as a hardware CPU using Logisim Evolution.

<h1>Features:</h1>
- 16-bit instruction format
- 5 general-purpose registers (including an accumulator)
- 256 bytes of memory
- Fully working hardware CPU (Logisim)
- Software interpreter (Python)
- Rich control flow:
- - JMP, JZ, JP, JN
- - COM (compare + branch)
- - GOTO (counted loop instruction)

<h1>Instruction format:</h1>
All instructions are 16 bits:
[ OPCODE (4 bits) ][ ARG1 (4 bits) ][ ARG2 (8 bits) ]

<h2>Instruction set opcodes</h2>
<ul>
<li>1 - Load [opcode][register][literal value (2 hexadecimals)]</li>
<li>2 - ADD [opcode][emptyspace][register1][register2]</li>
<li>3 - SUB [opcode][emptyspace][minuend][subtrahend]</li>
<li>4 - MOV [opcode][emptyspace][destination][source]</li>
<li>5 - LOADM [opcode][emptyspace][register][memoryaddr]</li>
<li>6 - JMP [opcode][emptyspace][address(2 bytes)]</li>
<li>7 - JZ [opcode][register][address(2 bytes)]</li>
<li>8 - JP [opcode][register][address(2 bytes)]</li>
<li>9 - JN [opcode][register][address(2 bytes)]</li>
<li>10 - COM [opcode][address][register1][register2]</li>
<li>11 - GOTO [opcode][address (2 bytes)][times to loop]</li>
<li>12 - SAVEM [opcode][emptyspace][register][memoryaddr]</li>
<li>13 - HLT</li>
<li>14 - OUT [opcode][emptyspace][emptyspace][register]</li>
</ul>

<h2>Example usage</h2>
<ul>
<li>1309 - Load the value 9 into register 3</li>
<li>2001 - Add together the contents of register 0 (ACC) and register 1</li>
<li>3021 - Subtract the contents of register 1 from register 2</li>
<li>4040 - Move the contents of register 0 (ACC) to register 4</li>
<li>502c - Copy the contents of memory address 12 to register 2</li>
<li>6050 - Jump to ROM address 0x50</li>
<li>7360 - If register 3 == 0, jump to line 60 (hexadecimal, literal is 96)</li>
<li>8370 - If register 3 is positive, jump to line 70</li>
<li>9380 - If register 3 is negative, jump to line 80</li>
<li>af32 - If register 3 = register 2 goto line 15 (f)</li>
<li>b2a4 - GOTO line 2a, 4 times</li>
<li>c0c3 - Save the contents of register 3 to memory address 12</li>
<li>d*** - Halt all processes (*** = any number can go here)</li>
<li>e**1 - Output the value in register 1 to the TTY in ASCII form</li>
</ul>
