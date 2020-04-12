from collections import defaultdict

_n = int(input())
radius = [int(x) for x in input().split()]

numbRadius = {}


def findNumb(n):
    if numbRadius.get(n):
        return numbRadius[n]
    count = 0
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if x ** 2 + y ** 2 <= n ** 2:
                count += 1


    numbRadius[n] = count

    return numbRadius[n]


integers = []

mod8 = [[], [], [], [], [], [], [], []]

for el in radius:
    n = findNumb(el)
    integers.append(n)
    mod8[n % 8].append(n)

for i in range(8):
    mod8[i].sort()

toomuch = sum(integers) % 8

if toomuch == 0:
    print(0)
    exit()

waysToWalk = [[[1]], [[2], [1, 1]], [[3], [1, 2], [1, 1, 1], [2, 1]],
              [[4], [1, 3], [1, 1, 2], [1, 1, 1, 1], [1, 2, 1], [2, 2], [2, 1, 1], [3, 1]],
              [[5], [1, 4], [1, 1, 3], [1, 1, 1, 2], [1, 1, 1, 1, 1], [1, 1, 2, 1], [1, 2, 2], [1, 2, 1, 1], [1, 3, 1],
               [2, 3], [2, 1, 2], [2, 1, 1, 1], [2, 2, 1], [3, 2], [3, 1, 1], [4, 1]],
              [[6], [1, 5], [1, 1, 4], [1, 1, 1, 3], [1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1], [1, 1, 2, 2],
               [1, 1, 2, 1, 1], [1, 1, 3, 1], [1, 2, 3], [1, 2, 1, 2], [1, 2, 1, 1, 1], [1, 2, 2, 1], [1, 3, 2],
               [1, 3, 1, 1], [1, 4, 1], [2, 4], [2, 1, 3], [2, 1, 1, 2], [2, 1, 1, 1, 1], [2, 1, 2, 1], [2, 2, 2],
               [2, 2, 1, 1], [2, 3, 1], [3, 3], [3, 1, 2], [3, 1, 1, 1], [3, 2, 1], [4, 2], [4, 1, 1], [5, 1]],
              [[7], [1, 6], [1, 1, 5], [1, 1, 1, 4], [1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 2, 1], [1, 1, 1, 2, 2], [1, 1, 1, 2, 1, 1], [1, 1, 1, 3, 1], [1, 1, 2, 3], [1, 1, 2, 1, 2],
               [1, 1, 2, 1, 1, 1], [1, 1, 2, 2, 1], [1, 1, 3, 2], [1, 1, 3, 1, 1], [1, 1, 4, 1], [1, 2, 4],
               [1, 2, 1, 3], [1, 2, 1, 1, 2], [1, 2, 1, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 2, 2], [1, 2, 2, 1, 1],
               [1, 2, 3, 1], [1, 3, 3], [1, 3, 1, 2], [1, 3, 1, 1, 1], [1, 3, 2, 1], [1, 4, 2], [1, 4, 1, 1], [1, 5, 1],
               [2, 5], [2, 1, 4], [2, 1, 1, 3], [2, 1, 1, 1, 2], [2, 1, 1, 1, 1, 1], [2, 1, 1, 2, 1], [2, 1, 2, 2],
               [2, 1, 2, 1, 1], [2, 1, 3, 1], [2, 2, 3], [2, 2, 1, 2], [2, 2, 1, 1, 1], [2, 2, 2, 1], [2, 3, 2],
               [2, 3, 1, 1], [2, 4, 1], [3, 4], [3, 1, 3], [3, 1, 1, 2], [3, 1, 1, 1, 1], [3, 1, 2, 1], [3, 2, 2],
               [3, 2, 1, 1], [3, 3, 1], [4, 3], [4, 1, 2], [4, 1, 1, 1], [4, 2, 1], [5, 2], [5, 1, 1], [6, 1]]]
smallest = -1

for ways in waysToWalk[toomuch - 1]:
    localSum = 0
    occurances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    try:
        for el in ways:
            localSum += mod8[el][occurances[el - 1]]
            occurances[el - 1] += 1

        if localSum <= smallest or smallest<0:
            smallest = localSum
    except:
        continue

if smallest == -1:
    print(sum(integers))
else:
    print(smallest)


'''
from collections import defaultdict
differentWays = defaultdict(list)

differentWays[1] = [[1]]
def waysToWalk(n):
    differentWays[n].append([n])
    if n==9:
        return 1
    for i in range(n, 1, -1):
        print(i)
        for lst in differentWays[i-1]:
            print(lst)
            differentWays[n].append([n-i+1]+lst)
    waysToWalk(n+1)

print(waysToWalk(2))
print(differentWays.values())
'''