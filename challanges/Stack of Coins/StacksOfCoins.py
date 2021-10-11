def solution(A):
    left = [0]*len(A)
    right = [0]*len(A)

    for i in range(len(A)-1):
        right[i+1] = (A[i] + right[i])//2
        
    j = len(A) - 1
    while j > 0:
        left[j-1] =  (A[j]+left[j])//2
        j -= 1
        
    max_ele = 0
    for i in range(len(A)):
        if A[i] + right[i]+left[i] > A[max_ele] + \
            right[max_ele]+left[max_ele]:
            max_ele = i
            
    return A[max_ele] + right[max_ele]+left[max_ele]


# sanity checks:
print(solution([3,7,0,5]))
print(solution([100,100,100,100]))
