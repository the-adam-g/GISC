#GRISC cpu simulator
#GRISC V1
#Codename - Lancaster

r1 = 0
r2 = 0
r3 = 0
r4 = 0

path = input()
contents = []
file = open(path, "r")
for line in file:
    contents.append(line.strip('\n'))
print(contents)

for i in range(len(contents)):
    currentins = contents[i].split(' ')
    print(currentins)
    match currentins[0]:
        case 'LOAD':
            if ((int(currentins[2]) < 5) and (int(currentins[2]) > 0)):
                match int(currentins[2]):
                    case 1:
                        r1 = int(currentins[1])
                        break
                    case 2:
                        r2 = int(currentins[1])
                        break
                    case 3:
                        r3 = int(currentins[1])
                        break
                    case 4:
                        r4 = int(currentins[1])
                        break
print(r1, r2, r3, r4)