

def run():
    for line in sorted(LINES, key=first):
        runLine(line[1])

def runLine(line):
    i = 0
    while i <= len(line)-1:
        e, j = runFunc(i, line)
        i+=j
        i += 1


def runFunc(i, line):
    if (funcId := search(FUNCS, line[i], key=first)) != None:
        values = []
        j = 0
        for j in range(FUNCS[funcId][1]):
            i+=1
            values.append(runFunc(i, line)[0])

        if FUNCS[funcId][1] == 0:
            result = FUNCS[funcId][2]()
        else:
            result = FUNCS[funcId][2](*values)

        return result, j+1
    
    elif line[i] == VARS:
        return VARS[i]
    
    elif isNumber(line[i]):
        return float(line[i]), 0
    
    else:
        raise ValueError(f'{line[i]} is not a function nor a variable')


def nothing(a):
    return a

def search(l, a, key=nothing):
    for i, e in enumerate(l):
        if key(e) == a:
            return i
    return None

def first(l):
    return l[0]

def isInt(s):
    try:
        int(s)
    except ValueError:
        return False
    return True

def isNumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def snipString(s, a):
    return a.join(snip(s.split(a), a))

def snip(n, a):
    if n[0] == '':
        n = snip(n[1:], a)
    elif n[-1] == '':
        n = snip(n[:-1], a)
    return n

def parse(line):
    cmd = line.split(' ')
    if isInt(cmd[0]):
        LINES.append([int(cmd[0]), line.split(' ')[1:]])
    else:
        runLine(line.split(' '))

FUNCS = [['print', 1, print], ['input', 1, input], ['run', 0, run]]
VARS = {'x': 5}
LINES = []

while True:
    line = snipString(input('>> '), ' ')
    parse(line)