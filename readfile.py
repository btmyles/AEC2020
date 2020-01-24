
import re
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
            x = [(fname[i], fname[i+1]) for i in range(0, columns*2, 2)]
            arr.append(x)

    return arr

print(readfile("SJs.txt"))
