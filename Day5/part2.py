import math

class Smoke:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if self.start[0] == self.end[0]:
            self.orientation = 0
        elif self.start[1] == self.end[1]:
            self.orientation = 1
        else:
            self.orientation = 2


tiles = []
f = open("input")
smokes = []
xMax = 0
yMax = 0
for x in f:
    x = x.replace("\n", "")
    x = x.split(" -> ")
    start = x[0].split(',')
    end = x[1].split(',')
    start[0] = int(start[0])
    start[1] = int(start[1])
    end[0] = int(end[0])
    end[1] = int(end[1])
    if start[0] == end[0] or start[1] == end[1] or math.atan(abs(end[1] - start[1]) / abs(end[0] - start[0])) * (180/math.pi) == 45.0:
        if start[0] > xMax:
            xMax = start[0]
        if end[0] > xMax:
            xMax = end[0]
        if start[1] > yMax:
            yMax = start[1]
        if end[1] > yMax:
            yMax = end[1]
        tmp = Smoke(start, end)
        smokes.append(tmp)
yMax += 1
xMax += 1
for x in range(yMax):
    tiles.append([0]*xMax)

for s in smokes:
    if s.orientation == 0:
        if s.start[1] < s.end[1]:
            for x in range(s.start[1], s.end[1] + 1):
                tiles[x][s.start[0]] += 1
        else:
            for x in range(s.end[1], s.start[1] + 1):
                tiles[x][s.start[0]] += 1
    elif s.orientation == 1:
        if s.start[0] < s.end[0]:
            for x in range(s.start[0], s.end[0] + 1):
                tiles[s.start[1]][x] += 1
        else:
            for x in range(s.end[0], s.start[0] + 1):
                tiles[s.start[1]][x] += 1
    else:
        dist = abs(s.start[0] - s.end[0])
        if s.start[1] < s.end[1] and s.start[0] < s.end[0]:
            for x in range(dist + 1):
                tiles[s.start[1] + x][s.start[0] + x] += 1
        if s.start[1] > s.end[1] and s.start[0] > s.end[0]:
            for x in range(dist + 1):
                tiles[s.start[1] - x][s.start[0] - x] += 1
        if s.start[1] < s.end[1] and s.start[0] > s.end[0]:
            for x in range(dist + 1):
                tiles[s.start[1] + x][s.start[0] - x] += 1
        if s.start[1] > s.end[1] and s.start[0] < s.end[0]:
            for x in range(dist + 1):
                tiles[s.start[1] - x][s.start[0] + x] += 1

count = 0
# msg = ""
for row in tiles:
    # msg += "\n"
    for p in row:
        # msg += "[" + str(p) + "]"
        if p > 1:
            count += 1
# print(msg)
print(count)