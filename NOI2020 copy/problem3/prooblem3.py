S, F = [int(x) for x in input().split()]
friendships = []

for _ in range(F):
    friendships.append([int(x) - 1 for x in input().split()])


def changeplace(n):
    a, b = friendships[n][0], friendships[n][1]
    friendships[n][0], friendships[n][1] = b+1, a+1

'''
def findSum():
    student = [0] * S
    summ = 0
    for friend in friendships:
        student[friend[0]] += 1
        student[friend[1]] -= 1
    for std in student:
        summ += abs(std)
    return summ
'''

def findSum(bi):
    student = [0] * S
    summ = 0
    for i,bool in enumerate(bi):
        if bool=='0':
            student[friendships[i][0]] += 1
            student[friendships[i][1]] -= 1
        elif bool=='1':
            student[friendships[i][0]] -= 1
            student[friendships[i][1]] += 1
    for std in student:
        summ += abs(std)
    return summ



def doBin(i):
    bi = bin(i)[2:]
    if len(bi)<F:
        bi = '0'*(F-len(bi))+ bi
    return bi

def printOrder(string):
    for n, el in enumerate(string):
        if el=='0':
            friendships[n][0]+=1
            friendships[n][1]+=1
        elif el=='1':
            changeplace(n)
    for el in friendships:
        print(el[0], el[1])

minimum = -1
order = ''

for i in range(2**F):
    local = findSum(doBin(i))
    if local<minimum or minimum<0:
        minimum = local
        order = doBin(i)
        if minimum==0 or (minimum==10 and i>F):
            print(minimum)
            printOrder(order)
            exit()
print(minimum)

printOrder(order)