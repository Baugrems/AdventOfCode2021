class Board: # object to hold a board matrix
    def __init__(self):
        self.matrix = []

    def printBoard(self):
        msg = ""
        for r in self.matrix:
            msg += "\n"
            for sq in r:
                if not sq.marked:
                    msg += "[" + sq.value + "] "
                else:
                    msg += "[X] "
        print(msg)


    def didIWin(self, value): # this function will check rows and columns to mark a value then look for a bingo. Returns boolean.
        newMark = False
        for r in self.matrix:
            for s in r:
                if value == s.value:
                    s.marked = True
                    newMark = True
                    break
        if not newMark:
            return False
        for r in self.matrix:
            bingo = True
            for sq in r:
                if not sq.marked:
                    bingo = False
                    break
            if bingo:
                return True
        for x in range(5):
            bingo = True
            for y in range(5):
                if not self.matrix[y][x].marked:
                    bingo = False
                    break
            if bingo:
                return True
        return False


        

class Square: # each square on a board is an object to hold its status and value
    marked = False
    value = 0
    def __init__(self, v):
        self.value = v

def runGame(boards, nums):
    for x in nums: # iterate over the random numbers until someone wins
        print("Drawn Number: " + x)
        for b in boards:
            b.printBoard()
            print("\n")
            if b.didIWin(x):
                return b, x

# Grab first line, our random bingo draws
f = open('input')
nums = f.readline()
nums = nums.replace("\n", "")
nums = nums.split(',')
print(nums)
# All set. Now to make boards

#Make board object and all boards array
bingo = Board()
boards = []
try:
    while True:
        line = f.readline()
        if not line:
            boards.append(bingo) # push completed board to array of boards
            break
        if line == "\n": # skip blank lines, and clear our board object to start new one
            # print("Blank")
            boards.append(bingo) # push completed board to array of boards
            del bingo
            bingo = Board()
        else:
            line = line.strip()
            line = line.split()
            row = []
            for x in line:
                sq = Square(x)
                row.append(sq)
            bingo.matrix.append(row)
except:
    pass
f.close()
boards.pop(0)
# for b in boards:
#     b.printBoard()
#     print("\n")


winner, num = runGame(boards, nums) # find winning board

sum = 0 # grab sum of unmarked spots
for r in winner.matrix:
    for sq in r:
        if not sq.marked:
            sum += int(sq.value)
print(sum * int(num))