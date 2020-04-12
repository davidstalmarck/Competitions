cases = int(input())

def SolveACase(case):
    n = int(input())

    lst = [[] for i in range(n)]
    k, r, c = 0, 0, 0

    for _ in range(n):
        row = input().split()

        # check if there is duplicate
        if len(row) != len(set(row)):
            r += 1

        # add the diagonal value
        k += int(row[_])

        for i in range(n):
            lst[i].append(row[i])

    for col in lst:
        if len(col) != len(set(col)):
            c += 1

    print('Case #' + str(case+1) + ':', k, r, c)


for i in range(cases):
    SolveACase(i)