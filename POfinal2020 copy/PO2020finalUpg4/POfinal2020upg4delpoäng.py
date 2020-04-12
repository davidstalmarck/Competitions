N, K = [int(x) for x in input().split()]

bestandsdelar = {i: set() for i in range(1, K + 1)}

celltyp = {}

for i in range(1, N + 1):
    string = input()
    celltyp[string] = i
    for k, j in enumerate(string):
        if j == '1':
            bestandsdelar[k + 1].add(string)



for i in range(int(input())):
    string = input()
    try:
        possibles = bestandsdelar[string.index('1') + 1]
    except:
        if N==1:
            print(1)
        else:
            print('vet ej')
        continue

    for k, j in enumerate(string):
        if j == '1':
            possibles = possibles.intersection(bestandsdelar[k + 1])




    length = len(possibles)
    if length == 0:
        print('finns ej')
    elif length == 1:
        print(celltyp[list(possibles)[0]])
    elif length > 1:
        print('vet ej')
