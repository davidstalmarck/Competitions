
antal_stolar, antal_par = [int(x) for x in input().split()]

#alla = [x+1 for x in range(antal_stolar)]
alla = {x:None for x in range(1, antal_stolar+1)}
lst_par = []
dict_par = {}

for i in range(antal_par):
    ett, tva = sorted([int(x) for x in input().split()])
    lst_par.append((ett, tva))
    #alla[ett-1], alla[tva-1] = False, False
    dict_par[tva]=ett

string = [0 for x in range(antal_stolar)]
def placera(n, count_ettor, count_tvaor):
    if n == antal_stolar + 1:
        print(string)
        exit()
    elif count_ettor + 1 <= count_tvaor:
        return ''
    elif count_ettor > count_tvaor+1:
        return ''
    elif dict_par.get(n):
        value = alla[dict_par[n]]
        if value == 1:
            string[n-1]=1
            placera(n + 1, count_ettor + 1, count_tvaor)

        elif value == 2:
            string[n-1]=2
            placera(n + 1, count_ettor, count_tvaor + 1)

    string[n-1]=1
    placera(n + 1, count_ettor + 1, count_tvaor)
    string[n-1]=2
    placera(n + 1, count_ettor, count_tvaor + 1)


print(placera(1, 0, 0))
'''
def placera(n, count_ettor, count_tvaor):
    print(count_ettor, count_tvaor)
    if n==antal_stolar+1:
        return ''
    
    elif dict_par.get(n):
        value = alla[dict_par[n]]
        if value == 1:
            placera(n + 1, count_ettor + 1, count_tvaor)
            
        elif value == 2:
            placera(n + 1, count_ettor, count_tvaor+1)
            
    elif count_ettor+1r<=count_tvaor:
        if count_ettor+1==count_tvaor:
            alla[n]=1
            placera(n + 1, count_ettor + 1, count_tvaor)

    elif count_ettor>count_tvaor:
        if count_tvaor+1==count_ettor:
            alla[n] = 2
            placera(n + 1, count_ettor, count_tvaor+1)
    




#count_ettor = 0
#count_tvaor = 0
'''
'''
def placera(n, count_ettor, count_tvaor):
    print(count_ettor, count_tvaor)
    if n==antal_stolar+1:
        return ''
    elif dict_par.get(n):
        value = alla[dict_par[n]]
        if value == 1:
            return '1' + placera(n + 1, count_ettor + 1, count_tvaor)
        elif value == 2:
            return '1' + placera(n + 1, count_ettor, count_tvaor+1)
    elif count_ettor<=count_tvaor:
        if count_ettor+1==count_tvaor:
            alla[n]=1
            placera(n + 1, count_ettor + 1, count_tvaor)
            return '1'
        else:
            placera(n-1, count_ettor, count_tvaor-1)
            return ''

    elif count_ettor>count_tvaor:
        if count_tvaor+1==count_ettor:
            alla[n] = 2
            return '2' + placera(n + 1, count_ettor, count_tvaor+1)
        else:
            return '' + placera(n, count_ettor-1, count_tvaor)


print(placera(1, 0, 0))

#count_ettor = 0
#count_tvaor = 0
'''
'''
def placera(n, count_ettor, count_tvaor):
    print(count_ettor, count_tvaor)
    if n==antal_stolar+1:
        if count_ettor + 1 == count_tvaor:
            return '2'
        elif count_ettor - 1 == count_tvaor:
            return '1'
        elif count_ettor == count_ettor:
            return '1'
        else:
            return None
    elif count_ettor+1==count_tvaor:
        return '2' + placera(n + 1, count_ettor, count_tvaor+1)

    elif count_ettor-1==count_tvaor:
        return '1' + placera(n + 1, count_ettor+1, count_tvaor)

    elif count_ettor == count_ettor:
        return '1' + placera(n + 1, count_ettor+1, count_tvaor)

    elif count_ettor == count_ettor:
        return '2' + placera(n + 1, count_ettor, count_tvaor + 1)
    elif count_ettor>count_tvaor:
        return placera(n-1, count_ettor-1, count_tvaor)
    elif count_tvaor>count_ettor:
        return placera(n - 1, count_ettor, count_tvaor-1)

print(placera(1, 0, 0))
'''
'''
count_ettor = 0
count_tvaor = 0
def placera(n):
    
    if count_ettor == count_tvaor:
        count_ettor +=1
        return '1' + placera(n)
        
    elif count_ettor > count_tvaor:

    elif count_ettor < count_tvaor:
    
'''