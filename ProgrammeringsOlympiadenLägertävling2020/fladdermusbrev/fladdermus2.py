N, Q, H, W = [int(x) for x in input().split()]

stolpar = []
for i in range(N):
    typ, x, y = [int(x) for x in input().split()]
    stolpar.append((typ, x, y))

stolpar.sort(key=lambda x: x[1])

# print(stolpar)

avstand_till_nasta_stolpe = {}


def distance_to_next_stolpe(at, next_stolpe):
    # print(at, next_stolpe)
    distance_x = next_stolpe[1] - at[0]
    next_y = next_stolpe[2]
    if next_stolpe[0] == 1:

        if at[1] >= next_stolpe[2]:
            next_y = at[1]
            distance_y = 0
        else:
            distance_y = next_stolpe[2] - at[1]
    else:

        if at[1] <= next_stolpe[2]:
            next_y = at[1]
            distance_y = 0
        else:
            distance_y = at[1] - next_stolpe[2]
    # print(distance_x, distance_y)
    return (next_stolpe[1], next_y), distance_x + distance_y


def check_last_one(from_pos, to_pos):
    # print(from_pos, to_pos)
    distance_x = to_pos[1] - from_pos[0]
    distance_y = abs(to_pos[2] - from_pos[1])
    # print(distance_x, distance_y)
    return distance_x + distance_y


def find_shortest_distance(from_pos, to_pos):
    distance = 0
    at = from_pos

    for stolpe in stolpar:
        if from_pos[0] < stolpe[1] < to_pos[1]:
            at, local_distance = distance_to_next_stolpe(at, stolpe)
            distance += local_distance

    local_distance = check_last_one(at, to_pos)
    distance += local_distance

    print(distance)


for k, stolpe in enumerate(stolpar[:-1]):
    dummy, avstand_till_nasta_stolpe[str(stolpe[1]) + '-' + str(stolpe[2])] = distance_to_next_stolpe(stolpe, stolpar[k + 1])

print(avstand_till_nasta_stolpe)
for i in range(Q):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    find_shortest_distance((x1, y1), [1, x2, y2])
