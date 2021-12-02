file = open("./input", "r")
previous = 0
count = 0
for x in file:
    if x > previous:
        count+=1
    previous = x
print(count)