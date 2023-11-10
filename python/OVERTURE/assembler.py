import re
import time

tijd = time.time_ns()

ass = open(r"python\OVERTURE\assembly.ovt", "r")
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

machine = open(r"Logisim\MachineCode.ovt", "w")
machine.write(x)
machine.close()

print(time.time_ns() - tijd)