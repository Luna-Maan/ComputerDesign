from pickle import TRUE
import time
import re
tijd = time.time()

ass = open(r"assembly.ovt", "r")
a = ass.read()
ass.close()

x = a.splitlines()
#print(x)

check = True
retreg = 31
importlist = []
while check:
    i = 0
    check = False
    for i in range(0,len(x)):
        if x[i].startswith("import"):
            path = r"Python\computer\\regi\programma's"
            path = path + "\\" + x[i][7:]
            if path not in importlist:
                importlist.append(path)
                bss = open(path, "r")
                b = bss.read()
                bss.close()
                y = b.splitlines()
                x.append('label ' + x[i][7:-4])
                x.pop(i)
                x = x+y
                x.append('ret')
                check = True
            else:
                x.pop(i)


#print(x)

x = [i for i in x if i]                     #remove all empty lines
for i in range(0,len(x)):                   #remove all comments
    index = re.search(";", x[i])
    string = x[i]
    if index != None:
        x[i] = string[:index.start()]
    else:
        pass
x = [i for i in x if i]

con = {}                                  #put all variables in con, then remove empty lines
LineNumber = 0
LabelLines = []
for i in range(0,len(x)):                 #put labels in the dictionary (con)
    parts = str.split(x[i])
    if parts[0] == 'label':
        con[parts[1]] = str(hex(LineNumber)[2:])
        LabelLines.append(x[i])
    elif parts[0] == 'function':
        con[parts[1]] = str(hex(LineNumber)[2:])
        LabelLines.append(x[i])
    elif parts[0] == 'const':             #put constants in the dictionary (con)
        con[parts[1]] = parts[2]
        LabelLines.append(x[i])
    else:
        LineNumber += 1
x = [line for line in x if line not in LabelLines]  #remove the lines of code with labels or constants
print(con)
#print(x)
for i in range(0,len(x)):
    #print(i)
    parts = str.split(x[i])
    #print(parts)
    for j in range(1,len(parts)):                      #replace variables with their value
        for key in con.keys():
            if parts[j] == key:
                parts[j] = con[key]
            if parts[j][1:-1] == key:
                parts[j] = '<' + con[key] + '>'
            if parts[j][2:-2] == key:
                parts[j] = '<<' + con[key] + '>>'
        if parts[j].startswith('0b'):
            parts[j] = hex(int(parts[j][2:], 2))
            parts[j] = str(parts[j][2:])
        elif parts[j].startswith('0d'):
            parts[j] = hex(int(parts[j][2:]))
            parts[j] = str(parts[j][2:])
        elif parts[j].startswith('0x'):
            parts[j] = str(parts[j][2:])
        else:
            pass

    parts[0] = parts[0].lower()
    if parts[0].startswith("jump"):                    #replace jump keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 1
        elif parts[0].endswith("eq"):
            parts[0] = 2
        elif parts[0].endswith("ge"):
            parts[0] = 3
        elif parts[0].endswith("lt"):
            parts[0] = 4
        elif parts[0].endswith("ne"):
            parts[0] = 5
        elif parts[0].endswith("le"):
            parts[0] = 6
        elif parts[0].endswith("jump"):
            parts[0] = 7
            if parts[1][0] != '<':
                parts[0] += 32
            parts.append('0')
            parts.append('0')
            parts[3] = parts[1]

            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            if parts[3][0] != '<':
                parts[0] += 32
        parts[0] = str(parts[0])

    if parts[0].startswith("ujump"):                    #replace unsigned jump keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 257
        elif parts[0].endswith("eq"):
            parts[0] = 258
        elif parts[0].endswith("ge"):
            parts[0] = 259
        elif parts[0].endswith("lt"):
            parts[0] = 260
        elif parts[0].endswith("ne"):
            parts[0] = 261
        elif parts[0].endswith("le"):
            parts[0] = 262
        elif parts[0].endswith("ujump"):
            parts[0] = 263
            if parts[1][0] != '<':
                parts[0] += 32
            parts.append('0')
            parts.append('0')
            parts[3] = parts[1]
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            if parts[3][0] != '<':
                parts[0] += 32
        parts[0] = str(parts[0])
    
    if parts[0].startswith("fjump"):                    #replace float jump keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 513
        elif parts[0].endswith("eq"):
            parts[0] = 514
        elif parts[0].endswith("ge"):
            parts[0] = 515
        elif parts[0].endswith("lt"):
            parts[0] = 516
        elif parts[0].endswith("ne"):
            parts[0] = 517
        elif parts[0].endswith("le"):
            parts[0] = 518
        elif parts[0].endswith("fjump"):
            parts[0] = 519
            if parts[1][0] != '<':
                parts[0] += 32
            parts.append('0')
            parts.append('0')
            parts[3] = parts[1]
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            if parts[3][0] != '<':
                parts[0] += 32       
        parts[0] = str(parts[0])
    
    if parts[0].startswith("call"):                    #replace call keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 1025
        elif parts[0].endswith("eq"):
            parts[0] = 1026
        elif parts[0].endswith("ge"):
            parts[0] = 1027
        elif parts[0].endswith("lt"):
            parts[0] = 1028
        elif parts[0].endswith("ne"):
            parts[0] = 1029
        elif parts[0].endswith("le"):
            parts[0] = 1030
        elif parts[0].endswith("call"):
            parts[0] = 1031
            if parts[1][0] != '<':
                parts[0] += 32
            parts.append('0')
            parts.append('0')
            parts[3] = parts[1]
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            if parts[3][0] != '<':
                parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0].startswith("icall"):                    #replace icall keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 3073
        elif parts[0].endswith("eq"):
            parts[0] = 3074
        elif parts[0].endswith("ge"):
            parts[0] = 3075
        elif parts[0].endswith("lt"):
            parts[0] = 3076
        elif parts[0].endswith("ne"):
            parts[0] = 3077
        elif parts[0].endswith("le"):
            parts[0] = 3078
        elif parts[0].endswith("icall"):
            parts[0] = 3079
            if parts[1][0] != '<':
                parts[0] += 32
            parts.append('0')
            parts.append('0')
            parts[3] = parts[1]
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            if parts[3][0] != '<':
                parts[0] += 32
        parts[0] = str(parts[0])
    
    if parts[0].startswith("ret"):                    #replace ret keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 1281
        elif parts[0].endswith("eq"):
            parts[0] = 1282
        elif parts[0].endswith("ge"):
            parts[0] = 1283
        elif parts[0].endswith("lt"):
            parts[0] = 1284
        elif parts[0].endswith("ne"):
            parts[0] = 1285
        elif parts[0].endswith("le"):
            parts[0] = 1286
        elif parts[0].endswith("ret"):
            parts[0] = 1287
            parts.append('0')
            parts.append('0')
            parts.append('0')
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            parts.append('0')
        parts[0] = str(parts[0])
    if parts[0].startswith("iret"):                    #replace iret keywords (loops)
        ha = False
        if parts[0].endswith("gt"):
            parts[0] = 3329
        elif parts[0].endswith("eq"):
            parts[0] = 3330
        elif parts[0].endswith("ge"):
            parts[0] = 3331
        elif parts[0].endswith("lt"):
            parts[0] = 3332
        elif parts[0].endswith("ne"):
            parts[0] = 3333
        elif parts[0].endswith("le"):
            parts[0] = 3334
        elif parts[0].endswith("iret"):
            parts[0] = 3335
            parts.append('0')
            parts.append('0')
            parts.append('0')
            ha = True
        if not ha:
            if parts[1][0] != '<':
                parts[0] += 128
            if parts[2][0] != '<':
                parts[0] += 64
            parts.append('0')
        parts[0] = str(parts[0])

    if parts[0].startswith("hlt"):                     #hlt
        parts[0] = str(1537)
    if parts[0].startswith("exit"):                    #exit
        parts[0] = str(1536)

    if parts[0] == "and":                             #and (logic)
        parts[0] = 8
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "or":                              #or
        parts[0] = 9
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "nand":                            #nand
        parts[0] = 10
        if parts[1][0] != '<':
            parts[0] += 128
        elif parts[2][0] != '<':
            parts[0] += 64
        elif parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "nor":                             #nor
        parts[0] = 11
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "xor":                             #xor
        parts[0] = 12
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "xnor":                            #xnor
        parts[0] = 13
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "test":                            #test
        parts[0] = 14
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "not":                             #not
        parts[0] = 15
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    if parts[0] == "high":                            #high
        parts[0] = 79
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    
    if parts[0] == "add":                             #add (arithmetic)
        parts[0] = 16
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "copy":                             #copy (arithmetic)
        parts[0] = 80
        if parts[1][0] != '<':
            parts[0] += 128
        elif parts[1][:2] == '<<':
            parts[0] = 1872
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[2] = '0'
        parts[0] = str(parts[0])
    if parts[0] == "concat":                            #concat
        parts[0] = 30
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])

    if parts[0] == "copyptr":                             #copyptr (arithmetic)
        parts[0] = 1872
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[2] = '0'
        parts[0] = str(parts[0])


    if parts[0] == "addc":                            #addc
        parts[0] = 17
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "sub":                             #sub
        parts[0] = 18
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "subb":                            #subb
        parts[0] = 19
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "mult":                            #mult
        parts[0] = 20
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "div":                             #div
        parts[0] = 21
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "inc":                             #inc
        parts[0] = 22
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    if parts[0] == "dec":                             #dec
        parts[0] = 23
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    
    if parts[0] == "fadd":                             #fadd (arithmetic)
        parts[0] = 528
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "fsub":                             #fsub (arithmetic)
        parts[0] = 529
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "fmult":                             #fmult (arithmetic)
        parts[0] = 530
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "fdiv":                             #fdiv (arithmetic)
        parts[0] = 531
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "ftoint":                             #ftoint (arithmetic)
        parts[0] = 532
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    if parts[0] == "inttof":                             #inttof (arithmetic)
        parts[0] = 533
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    if parts[0] == "fceil":                             #fceil (arithmetic)
        parts[0] = 534
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    if parts[0] == "fround":                             #fround (arithmetic)
        parts[0] = 534
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 32
        parts.append('0')
        parts[3] = parts[2]
        parts[0] = str(parts[0])
    
    if parts[0] == "shl":                             #shl (shifts&stack)
        parts[0] = 24
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "shlc":                            #shlc
        parts[0] = 25
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "shr":                             #shr
        parts[0] = 26
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "shrc":                            #shrc
        parts[0] = 27
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "rotl":                            #rotl
        parts[0] = 28
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "rotr":                            #rotr
        parts[0] = 29
        if parts[1][0] != '<':
            parts[0] += 128
        if parts[2][0] != '<':
            parts[0] += 64
        if parts[3][0] != '<':
            parts[0] += 32
        parts[0] = str(parts[0])
    if parts[0] == "push":                            #push
        parts[0] = 31
        if parts[1][0] != '<':
            parts[0] += 128
        parts[0] = str(parts[0])
    if parts[0] == "pop":                             #pop
        parts[0] = 63
        if parts[1][0] != '<':
            parts[0] += 128
        parts[0] = str(parts[0])

    x[i] = parts
#print(x)
for i in range(0,len(x)):
    print(x[i])
    for j in range(0, len(x[i])):

        if x[i][j][0] == '<':
            x[i][j] = x[i][j][1:-1]
            if x[i][j][0] == '<':
                x[i][j] = x[i][j][1:-1]
    x[i][0] = hex(int(x[i][0]))[2:]
    x[i] += ['0'] * (4 - len(x[i]))
    for j in range(0, len(x[i])):
        temp = len(x[i][j])
        x[i][j] = (4-temp)*str(0) + x[i][j]

    x[i] = ''.join(x[i])
    




string = ' '         #combine al instructions
x = string.join(x)

machine = open(r"MachineCode.out", "w")
machine.write(x)
machine.close()

machine = open(r"..\..\..\Logisim\MachineCode.ovt", "w")
machine.write(x)
machine.close()

x = x.replace(" ","\r\n")
x = "v2.0 raw\r\n" + x
machine = open(r"..\..\..\Digital\computer\RomData.hex", "w")
machine.write(x)
machine.close()
print(x)
print(time.time()-tijd)
input()