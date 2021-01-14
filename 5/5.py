import re
import math

with open("5/input.txt","r") as input:
    data = input.read().split("\n")
WIDTH = 8
HEIGHT = 128

def getNewRow(row, str):
    deep = 8-len(str)         
    if len(str) == 0:
        return row
    if str[0] == 'B':
        return getNewRow(row+(HEIGHT/(2**deep*2)), str[1:])
    if str[0] == 'F':
        return getNewRow(row-(HEIGHT/(2**deep*2)), str[1:])
    

def getNewCol(col, str):
    deep = 4-len(str)   
    if len(str) == 0:
        return col
    if str[0] == 'R':
        return getNewCol(col+(WIDTH/(2**deep*2)), str[1:])
    if str[0] == 'L':
        return getNewCol(col-(WIDTH/(2**deep*2)), str[1:])

def seatID(row, col):
    return row*8+col

maxID = 0
seatSet = set()

for x in data:
    seat = seatID(math.floor(getNewRow(HEIGHT/2, x[:-3])), math.floor(getNewCol(WIDTH/2, x[7:])))
    seatSet.add(seat)
for i in range(min(seatSet), max(seatSet)+1):
    if i not in seatSet:
        print(i)
    
  
