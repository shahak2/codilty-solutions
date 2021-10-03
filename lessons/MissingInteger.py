def solution(A):
    pos_counter  = [0]*(10**7)
    pos_counter[0] = 1
    for i in A:
        if i > 0:
            pos_counter[i] = 1
        else:
            continue
    for x in range(10**7):
        if pos_counter[x] == 0:
            return x
    return 1


