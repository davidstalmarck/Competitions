T, B = [int(x) for x in input().split()]

def Reversed(lst):
    return lst[::-1]

def Complemented(lst):
    newLst = []
    for el in lst:
        if el == '1':
            newLst.append('0')
        elif el == '0':
            newLst.append('1')
        else:
            newLst.append('*')
    return newLst

def Both(lst):
    return Complemented(Reversed(lst))

def CheckDiff123(lst1, lst2):
    if bool(set(lst1)-set(lst2)):
        return list(set(lst1)-set(lst2))[0]
    elif bool(set(lst2)-set(lst1)):
        return list(set(lst2)-set(lst1))[0]
    else:
        return list(set(lst1))[0]

def CheckDiff(lst1, lst2):
    differ = []
    for i in range(B):
        if lst1[i] != lst2[i]:
            if lst1[i] != '*' or lst2[i] != '*':
                differ.append(i)
    if len(differ)==0:
        return 0

    return differ[0]

def CheckWhatHappend(lst):

    rev, com, both = Reversed(lst), Complemented(lst), Both(lst)
    print(CheckDiff(rev, com) +1, flush=True)
    answer = input()
    if answer == rev[CheckDiff(rev, com)]:
        print(CheckDiff(rev, both) + 1, flush=True)
        answer = input()
        if answer == rev[CheckDiff(rev, both)]:
            print(CheckDiff(rev, lst) + 1, flush=True)
            answer = input()
            if answer == rev[CheckDiff(rev, lst)]:
                lst = rev
        else:
            print(CheckDiff(both, lst) + 1, flush=True)
            answer = input()
            if answer == both[CheckDiff(both, lst)]:
                lst = both
    else:
        print(CheckDiff(com, both) + 1, flush=True)
        answer = input()
        if answer == com[CheckDiff(com, both)]:
            print(CheckDiff(com, lst) + 1, flush=True)
            answer = input()
            if answer == com[CheckDiff(com, lst)]:
                lst = com
        else:
            print(CheckDiff(both, lst) + 1, flush=True)
            answer = input()
            if answer == both[CheckDiff(both, lst)]:
                lst = both

    return lst

def PlayOneRound(lst):
    lst = CheckWhatHappend(lst)
    checked=0
    for i in range(B):
        if checked==4:
            break
        if lst[i]=='*':
            print(i + 1, flush=True)
            lst[i] = input()
            checked += 1
    checked = 0
    for i in range(B-1, -1, -1):
        if checked==3:
            break
        if lst[i]=='*':
            print(i + 1, flush=True)
            lst[i] = input()
            checked += 1
    else:
        print(''.join(lst))
        answer = input()
        if answer == 'Y':
            return ['yes']
        else:
            exit()
    return lst

def SolveCase():
    lst = ['*' for _ in range(B)]
    for i in range(15):
        lst = PlayOneRound(lst)
        if lst[0]=='yes':
            return None
        else:
            continue
    print(''.join(lst))
    answer = input()
    if answer == 'Y':
        return ['yes']
    else:
        exit()

for i in range(T):
    SolveCase()
