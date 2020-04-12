from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(1000000000)

N, M, K = [int(x) for x in input().split()]

branches = defaultdict(list)

for i in range(N - 1):
    u, w = [int(x) for x in input().split()]
    if w == K:
        branches[w].append(u)
    elif u == K:
        branches[u].append(w)
    else:
        branches[u].append(w)
        branches[w].append(u)


def print_result(winners):
    winners.sort(key=lambda x: x[1])
    string = [str(el[0]) for el in winners] + [str(K)]
    print(' '.join(string))


possible_count = 0
possible_visited = {}


def check_if_possible(parent):
    global possible_count
    for el in branches[parent]:
        if possible_visited.get(el):
            continue
        else:
            possible_visited[el] = True
            countPostorder(el)
    possible_count += 1


visited = {}
visited_count = 0
give_number = 0


def check_children(child, parent):
    global visited_count, give_number

    if visited_count >= M - 1:
        print_result(list(visited.items()))
        exit()

    if visited.get(child):
        pass

    else:
        give_number += 1
        visited_count += 1
        visited[child] = give_number
        countPostorder(child)
        if visited.get(parent):
            give_number += 1
            visited[parent] = give_number


def countPostorder(parent):
    global give_number, visited_count

    if not visited.get(parent):
        give_number += 1
        visited_count += 1
        visited[parent] = give_number

    if visited_count >= M - 1:
        print_result(list(visited.items()))
        exit()

    for child in branches[parent]:
        check_children(child, parent)
        visited[parent] = visited_count


for el in branches[K]:
    possible_visited, possible_count = {}, 0
    visited, visited_count, give_number = {}, 0, 0
    check_if_possible(el)
    countPostorder(el)

    if possible_count >= M:
        countPostorder(el)

print(-1)



















'''
def countPostorder(parent):
    global visited_count
    
    for el in branches[parent]:
        
        if visited_count >=M-1:
            print_result(list(visited.items()))
            exit()


        if visited.get(el):
            #visited[el] = visited_count
            pass
        else:

            visited_count += 1

            visited[el] = visited_count

            countPostorder(el)
        visited[parent] = visited_count

'''

'''
for el in branches[K]:
    countPostorder(el)
    if len(subgraph) >= M-1:
        string = [K] + list(reversed(subgraph))[:M-1]
        print(' '.join([str(x) for x in string]))
        break
    subgraph = []
else:
    print(-1)

'''
