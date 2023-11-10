from PIL import Image
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(edgeitems=200)

img = Image.open(r"python\regi\bitmap\download.bmp")
ary = np.array(img)

print(ary)
temp = []
for i in range(0,len(ary)):
    for j in range(0,len(ary[i])):
        temp.append((ary[i][j][0]) // 8 * 32 * 32 + (ary[i][j][1]) // 8 * 32 + (ary[i][j][2]) // 8)
print(i,j)
for i in range(0,len(temp)):
    '''if temp[i] == 0:
        temp[i] += 2
    if temp[i] == 1:
        temp[i] = 0
    if temp[i] == 2:
        temp[i] = 1'''
    temp[i] = '(' + hex(temp[i])[2:] + ')'

temp = ' '.join(temp)

machine = open(r"python\regi\bitmap\bitmap.txt", "w")
machine.write(str(temp))
machine.close()