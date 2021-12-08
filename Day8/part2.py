class Segment:
    def __init__(self):
        self.a = ''
        self.b = ''
        self.c = ''
        self.d = ''
        self.e = ''
        self.f = ''
        self.g = ''
    def translate(self, segment):
        segment = sorted(segment)
        if segment == sorted(self.c + self.f):
            return '1'
        if segment == sorted(self.a + self.c + self.d + self.e + self.g):
            return '2'
        if segment == sorted(self.a + self.c + self.d + self.f + self.g):
            return '3'
        if segment == sorted(self.b + self.c + self.d + self.f):
            return '4'
        if segment == sorted(self.a + self.b + self.d + self.f + self.g):
            return '5'
        if segment == sorted(self.a + self.b + self.d + self.e + self.f + self.g):
            return '6'
        if segment == sorted(self.a + self.c + self.f):
            return '7'
        if segment == sorted(self.a + self.b + seg.c + self.d + seg.e + self.f + self.g):
            return '8'
        if segment == sorted(self.a + self.b + seg.c + self.d + self.f + self.g):
            return '9'
        if segment == sorted(self.a + self.b + seg.c + seg.e + self.f + self.g):
            return '0'
        print("oops", segment)
file = open("input")
total = 0
# file = ["edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"]
for x in file:
    seg = Segment()
    x = x.replace("\n", "")
    x = x.split(" | ")
    # print(x[0], x[1])
    x0 = x[0].split()
    for n in x0:
        if len(n) == 2: # segment is a 1
            count = 0
            for y in x0:
                if n[0] in y:
                    count += 1
            if count == 8:
                seg.c = n[0]
                seg.f = n[1]
            else:
                seg.c = n[1]
                seg.f = n[0]
    for n in x0:
        if len(n) == 3: # segment is a 7
            count = 0
            for c in n: # CNN ... get it?
                # print(c, seg.c, seg.f)
                if c == seg.c or c == seg.f:
                    continue
                else:
                    seg.a = c
    for n in x0:
        if len(n) == 4: # segment is a 4
            count = 0
            check = []
            for c in n:
                if c == seg.c or c == seg.f:
                    continue
                check.append(c)
            for y in x0:
                # print(check[0], y)
                if check[0] in y:
                    count += 1
            
            if count == 7:
                seg.d = check[0]
                seg.b = check[1]
            else:
                seg.d = check[1]
                seg.b = check[0]
    for n in x0:
        if len(n) == 7: # segment is an 8
            count = 0
            check = []
            for c in n:
                if c == seg.a or c == seg.b or c ==  seg.c or c == seg.d or c == seg.f:
                    continue
                check.append(c)
            for y in x0:
                if check[0] in y:
                    count += 1
            if count == 7:
                
                seg.g = check[0]
                seg.e = check[1]
            else:
                seg.g = check[1]
                seg.e = check[0]
    # print(seg.a, seg.b, seg.c, seg.d, seg.e, seg.f, seg.g)
    output = []
    
    for n in x[1].split():
        output.append(seg.translate(n))
    output = "".join(output)
    output = int(output)
    total += output
print(total)