N, d = [int(x) for x in input().split()]

m = {'01': 0, '02': 31, '03': 59, '04': 90, '05': 120, '06': 151, '07': 181, '08': 212, '09': 243, '10': 273, '11': 304,
     '12': 334}

b_dd, b_mm = input().split('/')

bjorne_start = int(b_dd) + m[b_mm]

bjorne_slut = bjorne_start + d


dagar_att_vakta, bjornar, dummy = {}, {}, {}



for i in range(bjorne_start, bjorne_slut):
    dagar_att_vakta[i%365]=[]

lst = []

for i in range(N-1):
    dd, mm = input().split('/')
    somnar = int(dd) + m[mm]-1
    vaknar = somnar + d + 1

    if dummy.get(somnar):
        continue
    else:
        dummy[somnar]=True
        bjornar[vaknar % 365] = (vaknar % 365, somnar % 365)
        lst.append((vaknar, somnar))



for i in lst:
    vaknar = i[0]
    somnar = i[1]
    for j in range(vaknar, somnar+365+1):
        if j%365 in dagar_att_vakta:
            dagar_att_vakta[j%365].append((vaknar%365, somnar%365))


prev = (bjorne_slut, (bjorne_start-1)%365)


def take_a_step(pre):
    earlier = None
    for i in range(366):
        if bjornar.get(i):
            earlier = bjornar[i]
        if i>pre[1]:
            if earlier==None:
                for j in range(365, -1, -1):
                    if bjornar.get(j):
                        return bjornar[j]
            elif earlier!=None:
                return earlier


# kolla ifall det inte fungerar
for day in dagar_att_vakta.values():
    if day == []:
        print(-1)
        exit()


winners = []
for day in dagar_att_vakta.values():
    if prev in day:
        continue
    else:
        prev = take_a_step(prev)
        winners.append(prev)

print(len(list(winners)))
