import re

ass = open(r"high.ovt", "r")
a = ass.read()
ass.close()

ass = open(r"pyemul.py", "r")
pyemul = ass.read()
ass.close()

a = a.split('\n')

for i in range(0, len(a)):
    a[i] = a[i].split(' ')

j=0
for i in range(0,len(a)):
    if len(a[j]) == 0:
        a.pop(j)
        j-=1
    elif a[j][0] == "const":
        a.pop(j)
        j-=1
    elif a[j][0] == "exit":
        a.pop(j)
        j-=1
    j+=1

for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if a[i][j] == "fwhile":
            a[i][j] = "while"


        if a[i][j] == "f=":
            a[i][j] = "="
        
        if a[i][j] == "inttof":
            a[i][j] = a[i][j+2]
            a[i][j+2] = a[i][j+1]
            a[i][j+1] = '='
        if "output" in a[i][j]:
            a[i][j] = a[i][j] + '('
            a[i][j+1] = ''
            a[i].append(')')



print(a)
for i in range(0,len(a)):
    a[i] = ' '.join(a[i])

for i in range(0,len(a)):
    if "array" in a[i]:
        a[i] = re.sub('[a](.*?)\(', '(', a[i])
        a[i] = a[i].replace('(','[')
        a[i] = a[i].replace(')',']')
        j=i+1
        while True:
            if a[j].replace(' ','').startswith('('):
                a[j] = a[j].replace('(','[')
                a[j] = a[j].replace(')',']')
                j+=1
            else:
                break
        


print(a)

a = '\n'.join(a)

pyemul = """import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((64,64))
#plt.imshow(a)
#plt.show(block = False)
#plt.pause(0.2)

count = 0
x=0
y=0
value = 1
def output2(b):
    global value
    value = int(b)

def output(b):
    global x
    x=int(b)
    print(x)

def output0(b):
    global x
    x=int(b)
    print(x)

def output1(b):
    global y
    global a
    global count
    y= int(b)
    a[x][y] = value
    count += 1
    if count % 1 == 0:
        plt.imshow(a)
        plt.show(block = False)
        plt.pause(0.01)
"""

print(pyemul + a)



machine = open(r"py.py", "w")
machine.write(pyemul + a)
machine.close()