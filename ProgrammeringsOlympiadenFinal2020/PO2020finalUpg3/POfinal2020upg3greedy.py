from itertools import permutations


antal_stolar, antal_par = [int(x) for x in input().split()]

#alla = [x+1 for x in range(antal_stolar)]


half = antal_stolar//2
lst = [x for x in ('1'*half + '2'*half)]

lst_par = []

#alla_lst = [x for x in range(1, antal_stolar+2)]
for i in range(antal_par):
    ett, tva = sorted([int(x) for x in input().split()])
    #lst_par.append(str(ett) + ' ' + str(tva))
    #alla_lst[ett - 1] = None
    #alla_lst[tva - 1] = None
    lst_par.append((ett, tva))


#kvar = [str(x) for x in alla_lst if x!=None]
#lst_par += kvar
lst_comb = [x for x in ('1'*half + '2'*half)]
if antal_stolar%2==0:
    for el in permutations(lst_comb, antal_stolar):
        for j, i in enumerate(lst_par):
            if el[i[0]-1]==el[i[1]-1] and abs(el.count[:j+1]('1')-el.count[:j+1]('2'))<=1:
                continue
            else:
                break
        else:
            print(''.join(el))

elif antal_stolar%2==1:
    lst_comb.insert(0, '1')
    so_far = []
    for el in permutations(lst_comb, antal_stolar):
        for j, i in enumerate(lst_par):
            if el[i[0]-1] == el[i[1]-1] and abs(el[:j+1].count('1')-el[:j+1].count('2'))<=1:
                continue
            else:
                break
        else:
            so_far = ''.join(el)
    lst_comb.pop(0)
    lst_comb.append('2')
    for el in permutations(lst_comb, antal_stolar):
        for j, i in enumerate(lst_par):
            if el[i[0]-1]==el[i[1]-1] and abs(el[:j+1].count('1')-el[:j+1].count('2'))<=1:
                continue
            else:
                break
        else:
            if int(''.join(el))>int(so_far):
                print(so_far)
                exit()
            else:
                print(int(''.join(el)))
                exit()



