from collections import defaultdict

N, Q = [int(x) for x in input().split()]

tillgangliga_a_b = defaultdict(list)

queries = []
count = 0
for i in range(Q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        count += 1
    queries.append(query)


def make_tillgangligt_g(a, b):
    tillgangliga_a_b[str(a) + '-' + str(b)].append([a, b])


def ta_bort_g(a, b):
    tillgangliga_a_b[str(a) + '-' + str(b)].pop()


def check_if_possible_g(x):
    for i in tillgangliga_a_b.values():
        if i != []:
            if x % i[0][1] == i[0][0]:
                print('Ja')
                break
    else:
        print('Nej')


tillgangliga_las = defaultdict(list)


def make_tillgangligt(a, b):
    for i in range(N // b + 1):
        i *= b
        tillgangliga_las[i + a].append(str(a) + '-' + str(b))


def ta_bort(a, b):
    for i in range(N // b + 1):
        i *= b
        tillgangliga_las[i + a].remove(str(a) + '-' + str(b))


def check_if_possible(x):
    if tillgangliga_las[x]:
        print('Ja')
    else:
        print('Nej')


if count <= 20:
    for query in queries:
        typ = query[0]
        if typ == 1:
            check_if_possible_g(query[1])

        elif typ == 2:
            make_tillgangligt_g(query[1], query[2])
        else:
            ta_bort_g(query[1], query[2])






else:
    for query in queries:
        typ = query[0]
        # print(query)
        if typ == 1:
            check_if_possible(query[1])

        elif typ == 2:
            make_tillgangligt(query[1], query[2])
        else:
            ta_bort(query[1], query[2])
        # print(tillgangliga_las)
