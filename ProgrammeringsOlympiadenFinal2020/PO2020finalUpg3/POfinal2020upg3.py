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

#print(graph)

def find_next(n):
    earlier_node = n
    try:
        next_node = graph[n].pop()
        if next_node>0:
            plusminus = 1
        else:
            plusminus = -1
        next_node = abs(next_node)

        graph[next_node].remove(earlier_node*plusminus)

        return earlier_node, next_node, plusminus
    except:
        return None, None, None



def inner_loop(n):

    earlier_node, next_node, plusminus = find_next(n)
    decided[earlier_node]=1

    while True:
        #print(earlier_node, next_node)
        if next_node == None:
            break
        if decided.get(next_node):
            if decided[next_node] == plusminus*decided[earlier_node]:
                break
            else:
                print(-1)
                exit()
        else:

            value = plusminus * decided[earlier_node]
            decided[next_node] = value

            earlier_node, next_node, plusminus = find_next(next_node)




for i in range(1, N + 1):
    if decided.get(i):
        #print(i)
        continue
    else:
        while graph[i]:
            inner_loop(i)



#print(decided)
order = sorted(list(decided.keys()))

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
        #print(-1)
        #exit()
        pass


print(string)

'''
    if decided.get(i):
        continue
    decided[i] = 1
    earlier_node = i
    try:
        next_node = graph[abs(earlier_node)].pop()
        dummy = graph[abs(next_node)].remove(abs(earlier_node))
    except:
        break
    while True:
        print(graph)
        print(next_node)
        if next_node > 0:
            decided[abs(next_node)] = decided[abs(earlier_node)]
        else:
            decided[abs(next_node)] = decided[abs(earlier_node)] * -1

        earlier_node = next_node
        try:
            next_node = graph[abs(earlier_node)].pop()
            dummy = graph[abs(next_node)].remove(abs(earlier_node))
        except:
            break

'''