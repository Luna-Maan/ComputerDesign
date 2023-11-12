import sys
import os
import string
from tokenize import ContStr

def shuntingyard(a):
    print(arrays)
    a = a.replace("(","( ")
    a = a.replace(")"," )")
    a = a.replace("]["," ) + ( ")
    a = a.replace("["," ( ")
    a = a.replace("]"," ) ) _ ")
    a = str.split(a)
    li = [arr[0] for arr in arrays if arr[0] in a]
    for i in range(0,len(arrays)):
        for j in range(0,len(a)):
            if arrays[i][0] in a[j]:
                if len(arrays[i]) == 3:
                    a[j] = '( *' + str(a[j]) + " + " + arrays[i][2] + " * "
                    #print(a)
                else:
                    pass
    
    a = ' '.join(a)
    a = str.split(a)

    operators = ["/", "*", "-", "+","&","|","^","nand","nor","xnor","_"]
    parsed = []
    stack = []
    while len(a) > 0:
        if a[0] not in operators and a[0] != "(" and a[0] != ")":
            parsed.append(a.pop(0))
        elif a[0] in operators:
            while len(stack) > 0:
                if stack[-1] == "(":
                    break
                elif (a[0] in ["/","*","_"]) and (stack[-1] in ["/","*","_"]):
                    parsed.append(stack.pop())
                elif (a[0] in ["+","-"]) and (stack[-1] in ["/","*","_","-","+"]):
                    parsed.append(stack.pop())
                elif (a[0] in ["&","|","^","nand","nor","xnor"]) and (stack[-1] in operators):
                    parsed.append(stack.pop())
                else:
                    break
            stack.append(a.pop(0))
        elif a[0] == "(":
            stack.append(a.pop(0))
        elif a[0] == ")":
            if len(stack) > 0:
                while stack[-1] != "(":
                    parsed.append(stack.pop())
                    if len(stack) == 0:
                        break
            stack.pop(-1)
            a.pop(0)

    while len(stack) > 0:
        parsed.append(stack.pop())
     
    instructions = []
    m = 0
    n = 0
    temp = 0
    while len(parsed)>1:
        n += 1
        if parsed[n] in operators:
            if parsed[n] == "*":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"mult " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"mult " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"mult " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
                m += 2
            elif parsed[n] == "_":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"copyptr " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"copyptr " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"copyptr " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                n -= 2
            elif parsed[n] == "/":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"div " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"div " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"div " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "-":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"sub " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"sub " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"sub " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "+":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"add " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"add " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"add " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "&":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"and " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"and " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"and " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "|":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"or " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"or " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"or " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "^":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"xor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"xor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"xor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "nand":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"nand " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"nand " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"nand " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "nor":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"nor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"nor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"nor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
            elif parsed[n] == "xnor":
                if str(parsed[n-1]).startswith("temp"):
                    instructions.insert(m,"xnor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-1]))
                elif str(parsed[n-2]).startswith("temp"):
                    instructions.insert(m,"xnor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " " + str(parsed[n-2]))
                else:
                    instructions.insert(m,"xnor " + str(parsed[n-2]) + " " + str(parsed[n-1]) + " temp" + str(temp))
                    temp += 1
                m += 1
                parsed.insert(n+1,"temp" + str(temp-1))
                parsed.pop(n)
                parsed.pop(n-1)
                parsed.pop(n-2)
                n -= 3
    return instructions

if len(sys.argv)==1:
    file_name = os.path.join(__file__, '../high.high')
else:
    file_name = sys.argv[1]
ass = open(file_name, "r")
a = ass.read()
ass.close()

dict = {}
arrays = []
arr = {}
x = a.splitlines()
i = 0
while True:
    if "+=" in x[i]:
        x[i] = x[i].replace("+=","=")
        parts = x[i].split()
        x[i] += (" + " + parts[0])
    elif "-=" in x[i]:
        x[i] = x[i].replace("-=","=")
        parts = x[i].split()
        x[i] += (" - " + parts[0])
    elif "*=" in x[i]:
        x[i] = x[i].replace("*=","=")
        parts = x[i].split()
        x[i] += (" * " + parts[0])
    elif "/=" in x[i]:
        x[i] = x[i].replace("/=","=")
        parts = x[i].split()
        x[i] += (" / " + parts[0])
    elif "&=" in x[i]:
        x[i] = x[i].replace("&=","=")
        parts = x[i].split()
        x[i] += (" & " + parts[0])
    elif "|=" in x[i]:
        x[i] = x[i].replace("|=","=")
        parts = x[i].split()
        x[i] += (" | " + parts[0])
    elif "^=" in x[i]:
        x[i] = x[i].replace("^=","=")
        parts = x[i].split()
        x[i] += (" ^ " + parts[0])
    elif "nand=" in x[i]:
        x[i] = x[i].replace("nand=","=")
        parts = x[i].split()
        x[i] += (" nand " + parts[0])
    elif "nor=" in x[i]:
        x[i] = x[i].replace("nor=","=")
        parts = x[i].split()
        x[i] += (" nor " + parts[0])
    elif "xnor=" in x[i]:
        x[i] = x[i].replace("snor=","=")
        parts = x[i].split()
        x[i] += (" xnor " + parts[0])
    
    if " = " in x[i].replace("  ",""):
        if any(ops in x[i] for ops in ["/", "*", "-", "+","&","|","^","nand","nor","xnor"]):
            tabs = len(x[i]) - len(x[i].lstrip())
            woord = x[i].split()[0]
            x[i] = x[i][tabs:]
            shuntedyard = shuntingyard(x[i][len(woord)+3:])
            ahh = len(shuntedyard)
            x[i:i] = shuntedyard
            for j in range(i, i + ahh):
                x[j] = "    " * (tabs//4) + x[j]
            tem = x[i+ahh-1].split()[:-1]
            tem.append(woord)
            x[i+ahh-1] = "    " * (tabs//4) + ' '.join(tem)
            #print(x)
            x.pop(i+ahh)
        elif "array" in x[i]:
            dims = x[i].count('[')
            x[i] = x[i].replace("array","")
            x[i] = x[i].replace(")","")
            x[i] = x[i].replace("(","")
            x[i] = x[i].replace(","," ")
            x[i] = x[i].replace("=","")
            x[i] = x[i].replace("["," ")
            x[i] = x[i].replace("]"," ")
            parts = x[i].split()
            pointer = parts.pop(0)
            l = True
            j=i
            while l:
                if len(x) > j+1:
                    if x[j+1].replace(" ","").startswith('('):
                        x[j] = x[j] + x[j+1]
                        x[j] = x[j].replace(")","")
                        x[j] = x[j].replace("(","")
                        x[j] = x[j].replace(",","")
                        x.pop(j+1)
                    else:
                        l = False
                else:
                    l = False
            if not pointer.startswith('<'):
                temp = [pointer]
                for k in range(0,dims):
                    temp.append(hex(int(parts[k],16)))
                arrays.append(temp)
                arr[temp[0]] = temp[1:]
            
            if pointer.startswith('<'):
                x.insert(i, "*copy " + str(pointer) +" pointer")
                x.pop(i+1)
                i+=1
                elements=1
                for j in range(0,dims):
                    elements *= parts[j]
                dict[pointer[1:-1]] = [0,elements,dims]
                for j in range(dims,len(parts)):
                    if j > dims:
                        x.insert(i, "inc pointer pointer")
                        i += 1
                    x.insert(i, "copy " + str(parts[j]) +" <pointer>")
                    i += 1
                i-=1
                
        else:
            tabs = len(x[i]) - len(x[i].lstrip())
            #print(tabs)
            x[i] = ("    " * (tabs//4)) + "copy " + x[i].split()[2] + " " + x[i].split()[0]
    if " f= " in x[i].replace("  ",""):
        if any(ops in x[i] for ops in ["/", "*", "-", "+","&","|","^","nand","nor","xnor"]):
            tabs = len(x[i]) - len(x[i].lstrip())
            woord = x[i].split()[0]
            #print(woord)
            x[i] = x[i][tabs:]
            shuntedyard = shuntingyard(x[i][len(woord)+4:])
            ahh = len(shuntedyard)
            x[i:i] = shuntedyard
            for j in range(i, i + ahh):
                x[j] = "    " * (tabs//4) + "f" + x[j]
                #print(x[j])
            tem = x[i+ahh-1].split()[:-1]
            tem.append(woord)
            x[i+ahh-1] = "    " * (tabs//4) + ' '.join(tem)
            x.pop(i+ahh)
    i+=1
    if i >= len(x):
        break
#print(arrays)

newloops = True
aantalloops = 0
while newloops==True:
    newloops = False
    i = 0
    while i < len(x):
        if x[i].startswith(("if","uif","fif")):
            if not x[i].startswith('i'):
                begin = x[i][0]
                x[i] = x[i][1:]
            else:
                begin = ''
            newloops = True
            x[i] = x[i].replace("if","")
            x[i] = x[i].replace(":","")
            if " >= " in x[i]:
                x[i] = x[i].replace(" >= "," ")
                x[i] = "jumplt" + x[i] + " loop" + str(aantalloops)
            if " <= " in x[i]:
                x[i] = x[i].replace(" <= "," ")
                x[i] = "jumpgt" + x[i] + " loop" + str(aantalloops)
            if " == " in x[i]:
                x[i] = x[i].replace(" == "," ")
                x[i] = "jumpne" + x[i] + " loop" + str(aantalloops)
            if " != " in x[i]:
                x[i] = x[i].replace(" != "," ")
                x[i] = "jumpeq" + x[i] + " loop" + str(aantalloops)
            if " < " in x[i]:
                x[i] = x[i].replace(" < "," ")
                x[i] = "jumpge" + x[i] + " loop" + str(aantalloops)
            if " > " in x[i]:
                x[i] = x[i].replace(" > "," ")
                x[i] = "jumple" + x[i] + " loop" + str(aantalloops)
            x[i] = begin + x[i]
            j = i+1
            while True:
                #print(x,j)
                if not x[j].startswith("    "):
                    break
                else:
                    x[j] = x[j].replace("    ", "",1)
                j += 1
                if j>=len(x):
                    break
            x.insert(j, "label loop" + str(aantalloops))
            x.insert(j, "jump end" + str(aantalloops))
            j += 2
            while j<len(x):
                if x[j].startswith("    ") or x[j].startswith("else:"):
                    x[j] = x[j].replace("    ","",1)
                    if x[j].startswith("else:"):
                        x.pop(j)
                        j -= 1
                    j += 1
                else:
                    break
            x.insert(j, "label end" + str(aantalloops))
            aantalloops += 1

        if x[i].startswith(("while","uwhile","fwhile")):
            if not x[i].startswith('w'):
                begin = x[i][0]
                x[i] = x[i][1:]
            else:
                begin = ''
            newloop = True
            x[i] = x[i].replace("while","")
            x[i] = x[i].replace(":","")
            x.insert(i,"label loop" + str(aantalloops))
            i += 1
            if " >= " in x[i]:
                x[i] = x[i].replace(" >= "," ")
                x[i] = "jumplt" + x[i] + " end" + str(aantalloops)
            if " <= " in x[i]:
                x[i] = x[i].replace(" <= "," ")
                x[i] = "jumpgt" + x[i] + " end" + str(aantalloops)
            if " == " in x[i]:
                x[i] = x[i].replace(" == "," ")
                x[i] = "jumpne" + x[i] + " end" + str(aantalloops)
            if " != " in x[i]:
                x[i] = x[i].replace(" != "," ")
                x[i] = "jumpeq" + x[i] + " end" + str(aantalloops)
            if " < " in x[i]:
                x[i] = x[i].replace(" < "," ")
                x[i] = "jumpge" + x[i] + " end" + str(aantalloops)
            if " > " in x[i]:
                x[i] = x[i].replace(" > "," ")
                x[i] = "jumple" + x[i] + " end" + str(aantalloops)
            j = i + 1
            x[i] = begin + x[i]
            while True:
                if x[j].startswith("    ") or x[j].startswith("else:"):
                    x[j] = x[j].replace("    ","",1)
                    j += 1
                else:
                    break
            x.insert(j, "label end" + str(aantalloops))
            x.insert(j, "jump loop" + str(aantalloops))
            aantalloops += 1

        if x[i].startswith("for"):
            newloop = True
            x[i] = x[i].replace("in","",1)
            x[i] = x[i].replace("range(","",1)
            x[i] = x[i].replace("):","",1)
            x[i] = x[i].replace(","," ")
            x[i] = x[i].replace("for","",1)
            parts = str.split(x[i])
            x.pop(i)
            x.insert(i, "label loop" + str(aantalloops))
            x.insert(i, "copy " + parts[1] + " " + parts[0])
            j = i+2
            while j < len(x):
                #print(x[j])
                if x[j].startswith("    "):
                    x[j] = x[j].replace("    ","",1)
                    j += 1
                else:
                    #print("___")
                    break
            x.insert(j, "jumplt " + parts[0] + " " + parts[2] + " loop" + str(aantalloops))
            if len(parts) == 4:
                x.insert(j, "add " + parts[0] + " " + parts[3] +" " + parts[0])
            else:
                x.insert(j, "inc " + parts[0] + " " + parts[0])
            aantalloops += 1
        i += 1

constants = []
labels = []
invalid = [32,33,34,35]
k=0
i = 0
while i < len(x):
    lijst = False
    parts = str.split(x[i])
    if len(parts) >= 1:
        if parts[0] == "label":
            labels.append(parts[1])
        if parts[0] == "const":
            invalid.append(int(parts[2],16))
            labels.append(parts[1])
    if len(parts) > 2:
        for j in range(1,len(parts)):
            if not parts[j].startswith(("0b","0x","0d","<0b","<0d","<0x")) and parts[0] != "const" and not all(c in string.hexdigits for c in parts[j]) and (not all(c in string.hexdigits for c in parts[j][1:-1]) or len(parts[j])<3):
                #print(parts[j])
                if parts[j].startswith("<"):
                    constants.append(parts[j][1:-1])
                else:
                    constants.append(parts[j])
                if 0 < j < len(parts)-1 and not parts[j].startswith('*') and not '[' in parts[1] and not parts[j].endswith('*'):
                    #print(parts[j])
                    parts[j] = "<" + parts[j] + ">"
                elif parts[j].startswith('*'):
                    parts[j] = parts[j][1:]
                elif parts[j].endswith('*'):
                    parts[j] = parts[j][:-1]
        if '[' in parts[1]:
            lijst = True
            dst = parts[2]
            parts = [parts[1]]
            parts[0] = parts[0].replace("["," ")
            parts[0] = parts[0].replace("]","")
            parts = parts[0].split(' ')
            temp = arr.get(parts[0])
            if len(parts) == 3:
                #print(dict)
                x[i] = "add " + str(parts[0]) + " <" + str(parts[2]) + "> adr"
                x.insert(i+1, "mult " + str(temp[1]) + " <" + str(parts[1]) + "> adr2")
                x.insert(i+2, "add <adr> <adr2> adr2")
                x.insert(i+3, "copy <adr2> " + dst)
                k=i+3
    if i >= k: 
        x[i] = ' '.join(parts)
    i += 1

constants = list(set(constants))
#print(invalid)
array_consts = []
for i in range(0,len(arrays)):
    temp = 1
    for j in range(1,len(arrays[i])):
        temp *= int(arrays[i][j],16)
        if j == 1:
            print(j, arrays, arrays[i][j])
    base  = 37
    while True:
        inv = False
        for j in range(0,int(temp)):
            if j+base in invalid:
                #print('h')
                inv = True
                break
        if inv == False:
            #print(base)
            break
        else:
            base += 1
    for j in range(0,int(temp)):
        invalid.append(j+base)
    array_consts.append("const " + str(arrays[i][0]) + " " + str(hex(base))[2:])
    dict[arrays[i][0]] = [base,temp,len(arrays[i])-1]
    #print(arrays[i][0])
    if str(arrays[i][0]) in constants:
        constants.remove(str(arrays[i][0]))



#print(constants)
j = 0
k = 0
for i in range(0,len(constants)):
    while k in invalid:
        k += 1
    if constants[j] in labels:
        constants.pop(j)
        j -= 1
        k -= 1
    else:
        if constants[j] == "output0" or constants[j] == "input0" or constants[j] == "output" or constants[j] == "input":
            constants[j] = "const " + constants[j] + " " + "20"
            k -= 1
        elif constants[j] == "output1" or constants[j] == "input1":
            constants[j] = "const " + constants[j] + " " + "21"
            k -= 1
        elif constants[j] == "output2" or constants[j] == "input2":
            constants[j] = "const " + constants[j] + " " + "22"
            k -= 1
        elif constants[j] == "output3":
            constants[j] = "const " + constants[j] + " " + "23"
            k -= 1
        elif constants[j] == "ram":
            constants[j] = "const " + constants[j] + " " + "25"
            k -= 1
        else:
            if constants[j] in dict:
                dict[constants[j]] = [k,dict[constants[j]][1],dict[constants[j]][2]]
            constants[j] = "const " + constants[j] + " " + str(hex(k))[2:]

    j += 1
    k += 1


k=0
#print(dict)
for i in range(0,len(x)):
    parts = str.split(x[k])
    if len(parts) > 0:
        if parts[0] in dict:
            x[k] = ''
            pointer = dict.get(parts[0])[0]
            l=0
            for j in range(1+dict.get(parts[0])[2],len(parts)):
                x.insert(k+l,"copy " + str(parts[j]) + " " + str(hex(pointer+l))[2:])
                l+=1
            k+=len(parts)-dict.get(parts[0])[2]-1
    k+=1




x = array_consts + constants + x
#print(x)
#print(labels)


x = '\n'.join(x)

if len(sys.argv)==1:
    file_name = os.path.join(__file__, '../assembly.rasm')
elif len(sys.argv)==3:
    name = "../" + sys.argv[2]
    print(name)
    input()
    file_name = os.path.join(__file__, name)
    print(file_name)
else:
    file_name = os.path.join(sys.argv[1], '../assembly.rasm')

if os.path.exists(file_name):
    machine = open(file_name, "w")
else:
    machine =  open(file_name, "x")
machine = open(file_name, "w")
machine.write(x)
machine.close()

print("compiled")