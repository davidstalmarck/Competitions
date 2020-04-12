cases = int(input())

def SolveCase(case):
    lst = [int(x) for x in input()]
    string = ''
    nestLevel = 0
    for el in lst:
        if nestLevel == el:
            pass

        elif nestLevel > el:
            while nestLevel > el:
                string += ')'
                nestLevel -= 1

        elif nestLevel < el:
            while nestLevel < el:
                string += '('
                nestLevel += 1

        string += str(el)

    while nestLevel>0:
        string += ')'
        nestLevel -=1
    print('Case #' + str(case+1) + ':', string)

for i in range(cases):
    SolveCase(i)

