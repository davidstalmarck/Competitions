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

    return newLst

def Both(lst):
    return Complemented(Reversed(lst))

def CheckDifferencesBetweenReversedComplemented(lst):
    revList, comList = Reversed(lst), Complemented(lst)
    differ = []
    for i in range(B):
        if revList[i] != comList[i]:
            differ.append(i)
    return differ

def CheckDifferencesBetweenReversedBoth(lst):
    revList, bothList = Reversed(lst), Both(lst)
    differ = []
    for i in range(B):
        if revList[i] != bothList[i]:
            differ.append(i)
    return differ

def CheckDifferencesBetweenComplementedBoth(lst):
    comList, bothList = Complemented(lst), Both(lst)
    differ = []
    for i in range(B):
        if comList[i] != bothList[i]:
            differ.append(i)
    return differ

def CheckDiffferenceBetweenAnB(lst1, lst2):
    return list(set(lst1)-set(lst2))

def SolveCase():
    lst = ['*' for i in range(B)]
    wantingToCheck, at = [], 0

    # take in new values
    for i in range(at, at+5):
        print(i + 1, flush=True)
        lst[i] = input()
    for i in range(B-1, B-6-at, -1):
        print(i + 1, flush=True)
        lst[i] = input()

    revCom, revBoth, comBoth = CheckDifferencesBetweenReversedComplemented(lst), CheckDifferencesBetweenReversedBoth(lst), CheckDifferencesBetweenComplementedBoth(lst)

    revComRevBoth = CheckDiffferenceBetweenAnB(revCom, revBoth)
    revComcomBoth = CheckDiffferenceBetweenAnB(revCom, comBoth)


    answer = input()
    if answer == 'Y':
        return None
    else:
        exit()


for i in range(T):
    SolveCase()
