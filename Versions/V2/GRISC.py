#GRISC cpu simulator
#GRISC V2
#Codename - Cambridge

r1 = 0
r2 = 0
r3 = 0
r4 = 0
acc = 0
path = input()
contents = []
file = open(path, "r")
for line in file:
    contents.append(line.strip('\n'))
print(contents)

i = 0
gotos = {}
while i < len(contents):
    currentins = contents[i].split(' ')
    print(currentins)
    match currentins[0]:
        case 'LOAD':
            if ((int(currentins[2]) < 5) and (int(currentins[2]) > -1)):
                match int(currentins[2]):
                    case 0:
                        acc = int(currentins[1])
                    case 1:
                        r1 = int(currentins[1])
                    case 2:
                        r2 = int(currentins[1])
                    case 3:
                        r3 = int(currentins[1])
                    case 4:
                        r4 = int(currentins[1])
        case 'ADD':
            if ((int(currentins[2]) < 5) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < 5) and (int(currentins[1]) > -1)):
                match int(currentins[1]):
                    case 0:
                        match int(currentins[2]):
                            case 0:
                                acc = acc + acc
                            case 1:
                                acc = acc + r1
                            case 2:
                                acc = acc + r2
                            case 3:
                                acc = acc + r3
                            case 4:
                                acc = acc + r4
                    case 1:
                        match int(currentins[2]):
                            case 0:
                                acc = r1 + acc
                            case 1:
                                acc = r1 + r1
                            case 2:
                                acc = r1 + r2
                            case 3:
                                acc = r1 + r3
                            case 4:
                                acc = r1 + r4
                    case 2:
                        match int(currentins[2]):
                            case 0:
                                acc = r2 + acc
                            case 1:
                                acc = r2 + r1
                            case 2:
                                acc = r2 + r2
                            case 3:
                                acc = r2 + r3
                            case 4:
                                acc = r2 + r4
                    case 3:
                        match int(currentins[2]):
                            case 0:
                                acc = r3 + acc
                            case 1:
                                acc = r3 + r1
                            case 2:
                                acc = r3 + r2
                            case 3:
                                acc = r3 + r3
                            case 4:
                                acc = r3 + r4
                    case 4:
                        match int(currentins[2]):
                            case 0:
                                acc = r4 + acc
                            case 1:
                                acc = r4 + r1
                            case 2:
                                acc = r4 + r2
                            case 3:
                                acc = r4 + r3
                            case 4:
                                acc = r4 + r4
        case 'MOV':
            if ((int(currentins[2]) < 5) and (int(currentins[2]) > -1)) and ((int(currentins[1]) < 5) and (int(currentins[1]) > -1)):
                match int(currentins[1]):
                    case 0:
                        match int(currentins[2]):
                            case 0:
                                acc = acc
                            case 1:
                                acc = r1
                            case 2:
                                acc = r2
                            case 3:
                                acc = r3
                            case 4:
                                acc = r4
                    case 1:
                        match int(currentins[2]):
                            case 0:
                                r1 = acc
                            case 1:
                                r1 = r1
                            case 2:
                                r1 = r2
                            case 3:
                                r1 = r3
                            case 4:
                                r1 = r4
                    case 2:
                        match int(currentins[2]):
                            case 0:
                                r2 = acc
                            case 1:
                                r2 = r1
                            case 2:
                                r2 = r2
                            case 3:
                                r2 = r3
                            case 4:
                                r2 = r4
                    case 3:
                        match int(currentins[2]):
                            case 0:
                                r3 = acc
                            case 1:
                                r3 = r1
                            case 2:
                                r3 = r2
                            case 3:
                                r3 = r3
                            case 4:
                                r3 = r4
                    case 4:
                        match int(currentins[2]):
                            case 0:
                                r4 = acc
                            case 1:
                                r4 = r1
                            case 2:
                                r4 = r2
                            case 3:
                                r4 = r3
                            case 4:
                                r4 = r4                        
        # TODO LOADM. case 'LOADM':
        # TODO JMP.
        # TODO JZ.
        # TODO JP.
        # TODO JN.
        # TODO COM.
        case 'COM':
            register1 = int(currentins[1])
            register2 = int(currentins[2])
            regs = [acc, r1, r2, r3, r4]
            if ((register1 < 5) and (register1 > -1) and (register2 < 5) and (register2 > -1)):
                if regs[register1] == regs[register2]:
                    i = int(currentins[3]) - 1
                    continue
        case 'GOTO':
            if len(currentins) > 2:
                limit = int(currentins[2])
                count = gotos.get(i, 0)
                if count >= limit:
                    break
                else:
                    gotos[i] = count + 1
            i = (int(currentins[1]) - 1)
            continue

        case 'HALT':
            input("Press enter to end execution and see results")
            break
    i = i + 1 
print(f"r1: {r1}, r2: {r2}, r3: {r3}, r4: {r4}, acc: {acc}")