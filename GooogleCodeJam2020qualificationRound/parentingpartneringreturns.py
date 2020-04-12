cases = int(input())

def SolveCase(case):
    n = int(input())

    lst = [[] for i in range(1441)]
    printOrder = {}
    order = ['*' for i in range(n)]

    for i in range(n):
        start, stop = [int(x) for x in input().split()]
        printOrder[start] = [stop, i]
        for j in range(start, stop):
            lst[j].append(i)

    # check if possible
    for el in lst:
        if len(el) > 2:
            print('Case #' + str(case + 1) + ': IMPOSSIBLE')
            #print('IMPOSSIBLE')
            break
    else:
        at = -1
        for i in range(1441):
            if printOrder.get(i) and at <= i:
                order[printOrder[i][1]] = 'C'
                at = printOrder[i][0]

        for i in range(n):
            if order[i] == '*':
                order[i] = 'J'
        print('Case #' + str(case + 1) + ':', ''.join(order))

for i in range(cases):
    SolveCase(i)
