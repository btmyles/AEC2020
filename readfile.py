
import re
from configComp import configComp

def readfile(filename):
    file = open(filename, 'r')
    count, arr = 0, []
    for line in file.readlines():
        count += 1

        if count == 4:
            fname = line.rstrip().split(',')
            columns = int(fname[0])

        if count > 4:
            fname = line.rstrip().split(',') #using rstrip to remove the \n
            x = [(float(fname[i]), int(fname[i+1])) for i in range(0, columns*2, 2)]
            arr.append(x)

    configComp(arr)

#print(readfile("SJs.txt"))
