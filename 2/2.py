import os
import re

data = open(os.getcwd() + "\\AdventOfCode\\2\\input.txt").read().split('\n')

parsedData = []

for x in data:

    parsedData.append(list(filter(None, re.split("[- :]", x))))
parsedData.pop()

count = 0


for x in parsedData:
    print(x)
    if(x[3][int(x[0])-1] != x[3][int(x[1])-1] 
    and (x[3][int(x[1])-1] == x[2] 
    or x[3][int(x[0])-1] == x[2])):
        print("found" + ' '.join(x))
        count += 1

print(count)
