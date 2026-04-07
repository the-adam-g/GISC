import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

rom = []
def interpret():
    output.delete("1.0", "end")
    output2.delete("1.0", "end")
    output3.delete("1.0", "end")
    rom.clear()
    contents = []
    file = inputf.get("1.0", tk.END)
    file = file.split('\n')
    for line in file:
        contents.append(line.strip('\n'))
        if len(contents[len(contents)-1]) < 1:
            contents.pop(len(contents)-1)
    print(contents)

    for line in contents:
        ins = line.split(' ')
        match ins[0]:
            case 'LOAD':
                rom.append("1" + str(ins[1]) + format(int(ins[2]), '02x'))
            case 'ADD':
                rom.append("20" + str(ins[1]) + str(ins[2]))
            case 'SUB':
                rom.append("30" + str(ins[1]) + str(ins[2]))
            case 'MOV':
                rom.append("40" + str(ins[1]) + str(ins[2]))
            case 'SAVEM':
                rom.append("50" + str(ins[1]) + format(int(ins[2]), '02x'))
            case 'LOADM':
                rom.append("c0" + format(int(ins[1]), '02x') + str(ins[2]))
            case 'JMP':
                rom.append("60" + format(int(ins[1]), '02x'))
            case 'JN':
                rom.append("9" + str(int(ins[1])) + format(int(ins[2]), '02x'))
            case 'JZ':
                rom.append("7" + str(int(ins[1])) + format(int(ins[2]), '02x'))
            case 'JP':
                rom.append("8" + str(int(ins[1])) + format(int(ins[2]), '02x'))
            case 'COM':
                rom.append("a" + format(int(ins[3]), 'x') + str(int(ins[1])) + str(int(ins[2])))
            case 'GOTO':
                rom.append("b" + format(int(ins[1]), '02x') + str(int(ins[2])))
            case 'HALT':
                rom.append("d000")

    i = 0
    gotos = {}
    registers = [0, 0, 0, 0, 0]
    memory = [0] * 256
    output.insert(END, f"Line - acc - r1 - r2 - r3 - r4 \n")
    while i < len(contents):
        output.insert(END, f"{i + 1} - {registers} \n")
        currentins = contents[i].split(' ')
        print(currentins)
        match currentins[0]:
            case 'LOAD':
                if ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    registers[int(currentins[1])] = int(currentins[2])
            case 'ADD':
                if ((int(currentins[2]) < len(registers)) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    registers[0] = registers[int(currentins[1])] + registers[int(currentins[2])]
            case 'SUB':
                if ((int(currentins[2]) < len(registers)) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    registers[0] = registers[int(currentins[1])] - registers[int(currentins[2])]
            case 'MOV':
                if ((int(currentins[2]) < len(registers)) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    registers[int(currentins[1])] = registers[int(currentins[2])]
            case 'SAVEM':
                if ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    addr = int(currentins[2])
                    if addr >= 0 and addr < len(memory):
                        memory[addr] = registers[int(currentins[1])]
            case 'LOADM':
                if ((int(currentins[2]) < len(registers)) and (int(currentins[2]) > -1)):
                    addr = int(currentins[1])
                    if addr >= 0 and addr < len(memory):
                        registers[int(currentins[2])] = memory[addr]
            case 'JMP':
                i = int(currentins[1])
                continue
            case 'JN':
                print(f"{i + 1} - {registers} \n")
                register = registers[int(currentins[1])]
                target = int(currentins[2])
                if register < 0:
                    i = target
                    continue
            case 'JZ':
                print(f"{i + 1} - {registers} \n")
                register = registers[int(currentins[1])]
                target = int(currentins[2])
                if register == 0:
                    i = target
                    continue
            case 'JP':
                print(f"{i + 1} - {registers} \n")
                register = registers[int(currentins[1])]
                target = int(currentins[2])
                if register > 0:
                    i = target
                    continue
            case 'COM':
                if ((int(currentins[2]) < len(registers)) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < len(registers)) and (int(currentins[1]) > -1)):
                    if registers[int(currentins[1])] != registers[int(currentins[2])]:
                        i = (int(currentins[3]) - 1)
            case 'GOTO':
                if len(currentins) > 2:
                    limit = int(currentins[2])
                    count = gotos.get(i, 0)
                    if count < limit:
                        gotos[i] = count + 1
                        i = (int(currentins[1]) - 1)
                        continue
            case 'HALT':
                break
        i = i + 1
    output2.insert(END, f"Memory \n {memory} \n")
    for i in range(len(rom)):
        output3.insert(END, f"{rom[i]} \n")

root = tk.Tk()
root.title("GISC Interpreter - Written by Adam Gillion 2026")
root.minsize(150, 150)
tk.Label(root, text="GISC Interpreter").grid(row=1, column=3, padx=5, pady=5)
tk.Label(root, text="GISC code here").grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, text="Output").grid(row=2, column=3, padx=5, pady=5)
tk.Label(root, text="Memory").grid(row=2, column=4, padx=5, pady=5)
tk.Label(root, text="GISC ROM instructions").grid(row=2, column=5, padx=5, pady=5)
inputf = scrolledtext.ScrolledText(root, height=10, width=50)
inputf.grid(row=3, column=1, padx=5, pady=5)
output = scrolledtext.ScrolledText(root, height=10, width=50)
output.grid(row=3, column=3, padx=5, pady=5)
output2 = scrolledtext.ScrolledText(root, height=10, width=50)
output2.grid(row=3, column=4, padx=5, pady=5)
output3 = scrolledtext.ScrolledText(root, height=10, width=50)
output3.grid(row=3, column=5, padx=5, pady=5)
run = tk.Button(root, text="Run", command=interpret)
run.grid(row=4, column=2, padx=5, pady=5)
root.mainloop()