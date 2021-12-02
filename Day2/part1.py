file = open("./input", "r")
horizontal = 0
depth = 0
for x in file:
    x = x.split()
    if x[0] == "forward":
        horizontal += int(x[1])
    elif x[0] == "up":
        depth -= int(x[1])
    else:
        depth += int(x[1])

print("Distance:", horizontal)
print("Depth:", depth)
print("Product:", depth*horizontal)