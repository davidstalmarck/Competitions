N, M = [int(x) for x in input().split()]

graph, decided = {}, {}


def add_same(n, m):
    if graph.get(n):
        graph[n].append(m)
    else:
        graph[n] = [m]
    if graph.get(m):
        graph[m].append(n)
    else:
        graph[m] = [n]


def add_different(n, m):
    if graph.get(n):
        graph[n].append(-m)
    else:
        graph[n] = [-m]
    if graph.get(m):
        graph[n].append(-n)
    else:
        graph[m] = [-n]


for i in range(1, N + 1):
    if i % 2 == 1:
        add_different(i, i + 1)

for i in range(M):
    a, b = [int(x) for x in input().split()]
    add_same(a, b)

# print(graph)

for i in range(1, N + 1):
    value = 1
    if decided.get(i):
        # print(i, decided[i])
        continue

    if decided.get(abs(graph[i][0])):
        value = -1 * (decided[abs(graph[i][0])])

    if len(graph[i]) == 2:
        par = graph[i][1]
        decided[par] = value
    decided[i] = value

# print(decided)
order = sorted(list(decided.keys()))
# print(order)
string = ''
count_one, count_two = 0, 0
for i in range(1, N + 1):
    if decided[i] == -1:
        count_two += 1
        string += '2'
    else:
        count_one += 1
        string += '1'
    if abs(count_two - count_one) > 1:
        print(-1)
        exit()

print(string)

'''

n, m = [int(x) for x in input().split()]

decided, stolar, par = {i: None for i in range(1, n + 1)}, {}, {}

for i in range(1, n+1):
    if i % 2 == 1: stolar[i] = 1
    else: stolar[i] = -1

for i in range(m):
    a, b = [int(x) for x in input().split()]
    if a>b:
        a, b = b, a
    par[a]=b
    par[b]=None


def set_value(x, plusminus):
    if decided[x+plusminus]:
        return -stolar[x+plusminus]
    else:
        return 1




for i in range(1, n+1):

    if i % 2 == 1:
        plusminus, paritet = 1, 'odd'
    else:
        plusminus, paritet = -1, 'even'


    if decided[i]!=None: value = decided[i]
    else: value = set_value(i, plusminus)
    print(value)

    if par.get(i)!=None:
        stolar[i], stolar[par[i]] = value, value

        if paritet == 'odd':
                stolar[i+plusminus] = -value
    elif par.get(i)==None:
        if paritet== 'odd':
            stolar[i + plusminus] = - value


print(stolar)
'''
