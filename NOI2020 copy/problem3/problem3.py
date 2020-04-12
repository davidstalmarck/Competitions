S, F = [int(x) for x in input().split()]
friendships = []
student = [0] * S
for _ in range(F):
    friendships.append([int(x) - 1 for x in input().split()])


def findSum(std):
    summ = 0
    for el in std:

        summ+=abs(el)
    return summ

minimal = -1

def BruteForce(n):
    global minimal
    if n>=F-1:
        print(student)
        if findSum(student)<minimal or minimal<0:
            minimal = findSum(student)
        return 0

    a, b = friendships[n][0], friendships[n][1]
    student[a]+=1
    student[b]-=1
    BruteForce(n+1)

    a, b = friendships[n][0], friendships[n][1]
    student[a] -= 2
    student[b] += 2
    if n==F-1:
        print(student)
        if findSum(student) < minimal or minimal < 0:
            minimal = findSum(student)

        return 0
BruteForce(0)

print(student)
print(minimal)