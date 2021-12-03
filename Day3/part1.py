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


file = open("./input", "r")
count1 = [0]*12
count0 = [0]*12
for x in file:
    x = split(x)
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
i = 0
gamma = []
epsilon = []
while i < len(count0):
    if count0[i] > count1[i]:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
    i += 1
gamma = [str(x) for x in gamma]
epsilon = [str(x) for x in epsilon]
gamma = int(('').join(gamma))
epsilon = int(('').join(epsilon))
print(gamma, epsilon)
gamma = binaryToDecimal(gamma)
epsilon = binaryToDecimal(epsilon)
print(gamma, epsilon)
print(epsilon * gamma)
