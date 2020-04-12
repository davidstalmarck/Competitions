N, K = [int(x) for x in input().split()]
lst = [0] * (2 ** (K + 1))
def bin_to_int(n): return int(n, base=2)
for i in range(1, N + 1): lst[bin_to_int(input())] = i
def inner_loop(ind, val):
    for i in range(K):
        if (ind >> i) % 2 == 1:
            if lst[ind - 2 ** i] == 0: lst[ind - 2 ** i] = val
            elif lst[ind - 2 ** i] != val: lst[ind - 2 ** i] = -1
for i in range(len(lst)):
    if lst[len(lst) - i - 1] == 0: continue
    inner_loop(len(lst) - i - 1, lst[len(lst) - i - 1])
for i in range(int(input())):
    query_val = lst[int(input(), base=2)]
    if query_val == 0:print('finns ej')
    elif query_val == -1:print('vet ej')
    else:print(query_val)