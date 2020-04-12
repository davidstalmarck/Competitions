N, Q, H, W = [int(x) for x in input().split()]

stolpar = [None] * (W+1)
for i in range(N):
    typ, x, y = [int(x) for x in input().split()]
    stolpar[x] = (typ, x, y)

#print(stolpar)


def distance_to_next_stolpe(at, next_stolpe):
    #print(at, next_stolpe)
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
    #print(distance_x, distance_y)
    return (next_stolpe[1], next_y), distance_x + distance_y


def check_last_one(from_pos, to_pos):
    #print(from_pos, to_pos)
    distance_x = to_pos[1] - from_pos[0]
    distance_y = abs(to_pos[2] - from_pos[1])
    #print(distance_x, distance_y)
    return distance_x + distance_y

def find_shortest_distance(from_pos, to_pos):
    distance = 0
    at = from_pos


    for i in range(from_pos[0], to_pos[1]):
        #print(i)
        if stolpar[i] == None:
            continue
        else:
            at, local_distance = distance_to_next_stolpe(at, stolpar[i])
        distance += local_distance

    local_distance = check_last_one(at, to_pos)
    distance += local_distance

    print(distance)


for i in range(Q):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x2<x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    find_shortest_distance((x1, y1), [1, x2, y2])






'''
def distance_to_next_stolpe(at, next_stolpe):
    print(at, next_stolpe)
    distance_x = next_stolpe[1] - at[0]

    if next_stolpe[0] == 1:
        
        if at[1] >= next_stolpe[2]:
            distance_y = 0
        else:
            distance_y = next_stolpe[2] - at[1]
    else:
        if at[1] <= (H-next_stolpe[2]):
            distance_y = 0
        else:
            distance_y = at[1] - (H - next_stolpe[2])
    print(distance_x, distance_y)
    return (next_stolpe[1], next_stolpe[2]), distance_x + distance_y
'''

