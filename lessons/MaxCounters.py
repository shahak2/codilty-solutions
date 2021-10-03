def solution(N, A):
    max_val = 0
    add = 0
    counter = [0]*N
    for i in A:
        #print(counter, max_val)
        if i < N + 1:
            if counter[i - 1] < add:
                counter[i - 1] = add
            counter[i - 1] += 1
            if counter[i - 1] > max_val:
                max_val = counter[i - 1]
        else:
            add = max_val
    return [n if n >= add else add for n in counter]

    return counters
    
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
            
        
    
