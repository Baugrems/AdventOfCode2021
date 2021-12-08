class Crab:
    def __init__(self, x):
        self.pos = x
    def calcFuel(self, x):
        dist = abs(self.pos - x)
        f = 0
        for x in range(dist):
            f += x + 1
        return f
crabs = []
file = open("input")
data = file.readline()
data = data.split(',')
maxH = 0
for c in data:
    if int(c) > maxH:
        maxH = int(c)
    crabs.append(Crab(int(c)))
bestFuel = 99999999999999999999999
for x in range(maxH):
    fuel = 0
    for crab in crabs:
        fuel += crab.calcFuel(x)
    if fuel < bestFuel:
        bestFuel = fuel
print(bestFuel)
