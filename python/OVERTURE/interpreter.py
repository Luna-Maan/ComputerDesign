import re

ass = open(r"MachineCode.out", "r")
a = ass.read()
ass.close()

code = str.split(a)
for i in range(0,len(code)):
    code[i] = bin(int(code[i], 16))[2:].zfill(8)

print(code)

a = [0,0,0,0,0,0,0]

for j in range(0,200):
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
                print(int(input()))
            else:
                print(a[src])
        else:
            if src == 7:
                a[dst] = int(input())
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
            a[3] = a[1] + a[2]
        elif temp == '5':
            a[3] = a[1] - a[2]

    if (code[i][0] == '1') and (code[i][1] == '1'):    #11
        temp = str(int(code[i][5:],2))
        if temp == '1':
            if a[3]>0:a[6]=a[0]
        elif temp == '2':
            if a[3]==0:a[6]=a[0]
        elif temp == '3':
            if a[3]>=0:a[6]=a[0]
        elif temp == '4':
            if a[3]<0:a[6]=a[0]
        elif temp == '5':
            if a[3]!=0:a[6]=a[0]
        elif temp == '6':
            if (a[3]-127)<=0:a[6]=a[0]
        elif temp == '7':
            a[6]=a[0]
    print(a)

