N, K = [int(x) for x in input().split()]
lst = [0] * (2 ** K)


def bin_to_int(n):
    return int(n, base=2)


for i in range(1, N + 1):
    dummy = bin_to_int(input())
    lst[dummy] = i


def inner_loop(ind, val):
    for i in range(K):
        if (ind >> i) % 2 == 1:
            local_ind = ind - 2 ** i
            if lst[local_ind] == 0:
                lst[local_ind] = val
            elif lst[local_ind] != val:
                lst[local_ind] = -1


for i in range(len(lst)):
    cur = len(lst) - i - 1
    val = lst[cur]
    if val == 0:
        continue
    inner_loop(cur, val)


for i in range(int(input())):
    query_val = lst[int(input(), base=2)]
    if query_val == 0:
        print('finns ej')
    elif query_val == -1:
        print('vet ej')
    else:
        print(query_val)

'''

def inner_loop(n, value):
    string = bin(n)[2:]
    while len(string) < K: string = '0' + string

    for k, i in enumerate(string):
        if i == '1':
            local = int(string[:k] + '0' + string[k + 1:], base=2)
            print(local)
            if lst[local] == None:
                lst[local] = value
            else:
                lst[local] = -1

'''
