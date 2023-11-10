import numpy as np
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

i = 9
while i != 0:
    output(  i )
    i = i - 1


input()