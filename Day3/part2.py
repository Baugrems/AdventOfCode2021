def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def split(word):
    return [char for char in word]


def findOxy(data, index, common):
    newdata = []
    newcommon = []
    count1 = [0]*12
    count0 = [0]*12
    if len(data) == 1 or index == len(common):
        return data
    for x in data:
        x = split(x)
        if str(x[index]) == common[index]:
            newdata.append(x)
    for x in newdata:
        i = 0
        while i < len(common):
            x[i] = int(x[i])
            if x[i] == 1:
                count1[i] += 1
            else:
                count0[i] += 1
            i += 1
    i = 0
    while i < len(count1):
        if count1[i] >= count0[i]:
            newcommon.append('1')
        else:
            newcommon.append('0')
        i += 1
    return findOxy(newdata, index + 1, newcommon)

def findC02(data, index, common):
    newdata = []
    newcommon = []
    count1 = [0]*12
    count0 = [0]*12
    if len(data) == 1 or index == len(common):
        return data
    for x in data:
        x = split(x)
        if str(x[index]) != common[index]:
            newdata.append(x)
    for x in newdata:
        i = 0
        
        while i < len(common):
            x[i] = int(x[i])
            if x[i] == 1:
                count1[i] += 1
            else:
                count0[i] += 1
            i += 1
    i = 0
    while i < len(count1):
        if count1[i] >= count0[i]:
            newcommon.append('1')
        else:
            newcommon.append('0')
        i += 1
    return findC02(newdata, index + 1, newcommon)


file = open("./input", "r")
oxy = []
c02 = []
data = []
count1 = [0]*12
count0 = [0]*12
for x in file:
    x = split(x)
    data.append(x)
    i = 0
    if x[-1] == '\n':
        x.pop()
    while i < len(x):
        x[i] = int(x[i])
        if x[i] == 1:
            count1[i] += 1
        else:
            count0[i] += 1
        i += 1
common = []
i = 0
while i < len(count1):
    if count1[i] >= count0[i]:
        common.append('1')
    else:
        common.append('0')
    i += 1
# print("Most common string: ", common, "of length ", len(common))
# print(findOxy(data,0,common))
oxy = findOxy(data, 0, common)[0]
oxy = [str(x) for x in oxy]
oxy = int(('').join(oxy))
oxy = binaryToDecimal(oxy)
c02 = findC02(data, 0, common)[0]
c02 = [str(x) for x in c02]
c02 = int(('').join(c02))
c02 = binaryToDecimal(c02)
print(oxy, c02, oxy * c02)