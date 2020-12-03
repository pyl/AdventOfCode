
f = open("AdventOfCode/input.txt", "r")

firstArray = []

for x in f:
    firstArray.append(int(x))



for x in firstArray:
    for y in firstArray:
        for z in firstArray:
            if int(x+y+z) == 2020:
                print(x*y*z)