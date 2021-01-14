import re
with open("4/input.txt","r") as input:
    data = input.read().split("\n\n")
def validate(field, value):
    if field == 'byr':
        if int(value) >= 1920 and int(value) <= 2002:
            print("1", field, value)
            return True
    if field == 'iyr':
        if int(value) >= 2010 and int(value) <= 2020:
            print("2", field, value)
            return True
    if field == 'eyr':
        if int(value) >= 2020 and int(value) <= 2030:
            print("3", field, value)
            return True
    if field == 'hgt':
        if value[-2:] == "cm":
            if 150 <= int(value[:-2]) <= 193:
                print("4", field, value)
                return True 
        if value[-2:] == "in":
            if 59 <= int(value[:-2]) <= 76:
                print("5", field, value)
                return True 
    if field == 'hcl':
        letters = {'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        print("Check it")
        print(field, value)
        flag = True
        for x in value[1:]:
            if x not in letters:
                flag = False
        if value[0] == "#" and flag:
            print("Stop. 6", field, value)
            return True
    if field == 'ecl':
        eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        if value in eyes:
            return True
    if field == 'pid':
        if value.isnumeric() and len(value) == 9:
            return True
    print("Fails", field, value)
    return False
myset = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
counter = 0
for x in data:
    y = re.split("[ \n]", x) 
    fieldsInSet = 0
    numOfValid = 0
    for z in y:
        if z[:3] in myset:
            fieldsInSet += 1
        if validate(z[:3], z[4:]):
            numOfValid += 1 
    print(numOfValid)
    if fieldsInSet >= 7 and numOfValid >= 7:
        counter+=1
#     print(numOfValid)
print(counter)