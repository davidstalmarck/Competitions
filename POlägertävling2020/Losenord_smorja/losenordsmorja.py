K = input()

num1 = input().split()

seq1, len1 = num1[0], int(num1[1])

len_seq1 = len(seq1)

delta1 = len1 - len_seq1


num2 = input().split()

seq2, len2 = num2[0], int(num2[1])
len_seq2 = len(seq2)
delta2 = len2 - len_seq2


differance_between_1_and_2 = abs(len_seq1 - len_seq2)
differance_total = abs(len2-len1)

def make_string(len_string, len_other_string):
    winner = 'a'*len_string + '<'*(len_string-differance_between_1_and_2) + 'a'*len_other_string
    print(winner)



if len_seq1>=len_seq2 and differance_between_1_and_2>=differance_total:
    make_string(len1, len_seq2)

elif len_seq2>=len_seq1 and delta2 >= delta1:
    make_string(len2, len_seq1)


elif len_seq2==len_seq1:
    print(seq2)
else:
    print('!')
