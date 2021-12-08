

file = open("input")
count = 0
for x in file:
    x = x.split("|")[1]
    x = x.split()
    #print(x)
    for s in x:
        if len(s) == 2 or len(s) == 4 or len(s) == 3 or len(s) == 7:
            count += 1

print(count)