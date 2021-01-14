import re
import math

with open("6/input.txt","r") as input:
    data = input.read().split("\n\n")



sum = 0

for x in data:
    #create empty set
    parsedData = x.split("\n")
    allChars = set()
    for x in parsedData:
        for y in x:
            allChars.add(y)

    for x in allChars.copy():
        for y in parsedData:
            if x not in y:
                try:
                    allChars.remove(x)
                except:
                    pass
                
    sum += len(allChars)

print(sum)



    