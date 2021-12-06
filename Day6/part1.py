fish = { # map of fishies
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0
}

file = open("input")
data = file.readline().split(',')
for x in data:
    x = int(x)
    fish[x] += 1
# print("Initial", fish)
days = 256
for x in range(days):
    first = fish[1]
    for f in range(1,8):
        fish[f] = fish[f + 1]
    fish[8] = fish[0]
    fish[6] += fish[0]
    fish[0] = first
    # print(fish) 
count = 0
for x in range(9):
    count += fish[x]
print(count)