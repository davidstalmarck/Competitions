K = input()

seq1, total1 = input().split()

total1 = int(total1)

seq2, total2 = input().split()

total2 = int(total2)

if len(seq1) > len(seq2) and total1 < total2:
    print('!')


elif len(seq1) < len(seq2) and total1 > total2:

    print('!')


else:
    bigger_seq = max(seq1, seq2, key=lambda x: len(x))
    bigger_total = max(total1, total2)
    smaller_seq = min(seq1, seq2, key=lambda x: len(x))
    smaller_total = min(total1, total2)

    bigger_length = len(bigger_seq)

    smaller_length = len(smaller_seq)

    delta_length_seq = bigger_length - smaller_length

    delta_total = bigger_total - smaller_total

    if delta_total >= delta_length_seq or (bigger_length == bigger_total and smaller_length == smaller_total):
        winner = bigger_total * 'a'

        winner += (bigger_total - delta_length_seq) * '<'
        winner += smaller_length * 'a'
        print(winner)
    else:
        print('!')
