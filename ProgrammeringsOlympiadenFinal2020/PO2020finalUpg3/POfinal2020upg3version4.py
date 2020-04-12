from itertools import product, permutations, combinations_with_replacement

N, K = [int(x) for x in input().split()]

lst = [0] * (2 ** K)

for i in range(1, N+1):
    a = int(input(), base=2)
    lst[a] = i


def inner_loop(n, value):
    string = bin(n)[2:]

    while len(string) < K: string = '0' + string
    for k in range(K):
        if string[K-k-1]=='1':
            local = n ^ 2**k
            position = lst[local]

            if position == 0:
                lst[local] = value
            else:
                lst[local] = -1


big = 2 ** (K)-1
for k, i in enumerate(reversed(lst)):
    if i == 0:
        continue
    else:
        inner_loop(big - k, i)


print([el for el in reversed(lst)])

for i in range(int(input())):
    query = lst[int(input(), base=2)]

    #    print(int(input(), base=2))
    if query == 0:
        print('finns ej')
    elif query == -1:
        print('vet ej')
    else:
        print(query)
