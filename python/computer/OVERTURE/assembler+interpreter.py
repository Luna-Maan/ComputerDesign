import re

ass = open(r"assembly.ovt", "r")
a = ass.read()
ass.close()

x = re.sub("(?i)\nor",  "\n80", a)          #replace keywords
x = re.sub("(?i)\nnand","\n81", x)
x = re.sub("(?i)\nnor", "\n82", x)
x = re.sub("(?i)\nand", "\n83", x)
x = re.sub("(?i)\nadd", "\n84", x)
x = re.sub("(?i)\nsub", "\n85", x)

x = re.sub("(?i)\njump >0" , "\nc1", x)
x = re.sub("(?i)\njump =0" , "\nc2", x)
x = re.sub("(?i)\njump >=0", "\nc3", x)
x = re.sub("(?i)\njump <0" , "\nc4", x)
x = re.sub("(?i)\njump !=0", "\nc5", x)
x = re.sub("(?i)\njump <=0", "\nc6", x)
x = re.sub("(?i)\njump"    , "\nc7", x)

x = re.sub("(?i)\ncopy", "\n40", x)

x = re.sub("(?i)\nimme", "\n0", x)

x = x.splitlines()
x = [i for i in x if i]                     #remove all empty lines
for i in range(0,len(x)):                   #remove all comments
    index = re.search(";", x[i])
    string = x[i]
    if index != None:
        x[i] = string[:index.start()]
    else:
        pass

con = {}
LineNumber = 0
LabelLines = []
for i in range(0,len(x)):                 #put labels in the dictionary (con)
    parts = str.split(x[i])
    if parts[0] == 'label':
        con[parts[1]] = str(hex(LineNumber))
        LabelLines.append(x[i])
    elif parts[0] == 'const':             #put constants in the dictionary (con)
        con[parts[1]] = parts[2]
        LabelLines.append(x[i])
    else:
        LineNumber += 1

x = [line for line in x if line not in LabelLines]  #remove the lines of code with labels or constants

for i in range(0,len(x)):
    temp = 0
    parts = str.split(x[i])                            #split the line into keywords
    for j in range(0,len(parts)):                      #replace variables with their value
        for key in con.keys():   
            parts[j] = parts[j].replace(key, con[key])
    if len(parts) == 3:
        parts[1] = str(hex(int(parts[1],16)*8))[2:]
    for j in range(0,len(parts)):                      #add the value of the keywords together
        temp += int(parts[j],16)
    x[i] = hex(temp)[2:]

string = ' '
x = string.join(x)
print(x)

machine = open(r"MachineCode.out", "w")
machine.write(x)
machine.close()

ass = open(r"MachineCode.out", "r")
a = ass.read()
ass.close()

code = str.split(a)
for i in range(0,len(code)):
    code[i] = bin(int(code[i], 16))[2:].zfill(8)

print(code)

a = [0,0,0,0,0,0,0]

for j in range(0,100000):
    i = a[6]
    if i >= len(code):
        print("done")
        break
    a[6] += 1
    if (code[i][0] != '1') and (code[i][1] != '1'):    #00
        a[0] = int(code[i][2:],2)

    if (code[i][0] != '1') and (code[i][1] == '1'):    #01
        dst = int(code[i][5:],2)
        src = int(code[i][2:5],2)
        if dst == 7:
            if src == 7:
                print(int(input("input: ")))
            else:
                print("output:" + str(a[src]))
        else:
            if src == 7:
                a[dst] = int(input("input: "))
            else:
                a[dst] = a[src]

    if (code[i][0] == '1') and (code[i][1] != '1'):    #10
        temp = str(int(code[i][5:],2))
        if temp == '0':
            a[3] = a[1] | a[2]
        elif temp == '1':
            a[3] = ~(a[1] & a[2]) & 0xff
        elif temp == '2':
            a[3] = ~ (a[1] | a[2]) & 0xff
        elif temp == '3':
            a[3] = a[1] & a[2]
        elif temp == '4':
            a[3] = (a[1] + a[2]) % 256
        elif temp == '5':
            a[3] = (a[1] - a[2]) % 256

    if (code[i][0] == '1') and (code[i][1] == '1'):    #11
        temp = str(int(code[i][5:],2))
        if temp == '1':
            if a[3]>0:a[6]=a[0]-1
        elif temp == '2':
            if a[3]==0:a[6]=a[0]-1
        elif temp == '3':
            if a[3]>=0:a[6]=a[0]-1
        elif temp == '4':
            if a[3]<0:a[6]=a[0]-1
        elif temp == '5':
            if a[3]!=0:a[6]=a[0]-1   
        elif temp == '6':
            if a[3]<=0:a[6]=a[0]-1
        elif temp == '7':
            a[6]=a[0]
    print(a)

a = input()
print(a)