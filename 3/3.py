with open("3/input.txt","r") as input:
    data = input.read().split("\n")
data.pop()
WIDTH = len(data[0])
def thing(right, down):
    counter = 0
    row = 0
    col = 0
    for row,x in enumerate(data):
        if(row%down == 0):
            if(x[col%(WIDTH)] == "#"):
                counter+=1
            col += right
    return counter
print(thing(1,1)*thing(3,1)*thing(5,1)*thing(7,1)*thing(1,2))


