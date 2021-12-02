file = open("./input", "r")

count = 0
windowCount = 0
windows = []
sumW = 0
tmp = []
for x in file:
    if len(tmp) < 3:
        tmp.append(int(x))
    else:
        for y in tmp:
            sumW += y
        windows.append(sumW)
        sumW = 0
        tmp = [tmp[1], tmp[2], int(x) ]

previous = 0
for w in windows:
    print(w)
    if w > previous:
        count +=1
    previous = w
print(count)