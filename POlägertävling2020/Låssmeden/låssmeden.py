from collections import defaultdict
N, Q = [int(x) for x in input().split()]


tillgangliga_las = defaultdict(list)

def make_tillgangligt(a, b):
    for i in range(N//b + 1):
        i *=b
        tillgangliga_las[i + a].append(str(a) +'-'+ str(b))

def ta_bort(a, b):
    for i in range(N // b + 1):
        i *=b
        tillgangliga_las[i + a].remove(str(a) + '-' + str(b))

def check_if_possible(x):
    if tillgangliga_las[x]:
        print('Ja')
    else:
        print('Nej')

for i in range(Q):
    query = [int(x) for x in input().split()]
    typ = query[0]
    #print(query)
    if typ == 1:
        check_if_possible(query[1])

    elif typ == 2:
        make_tillgangligt(query[1], query[2])
    else:
        ta_bort(query[1], query[2])
    #print(tillgangliga_las)