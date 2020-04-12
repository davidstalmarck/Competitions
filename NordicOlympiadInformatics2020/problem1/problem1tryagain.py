from itertools import combinations
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