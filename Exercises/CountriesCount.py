    
def visit(A, row, col):
    color = A[row][col]
    stack = []
    stack.append((row,col))
    while stack != []:
        s = stack.pop()
        A[s[0]][s[1]] = None
        if s[0] + 1 < len(A) and A[s[0] + 1][s[1]] == color:
            stack.append((s[0] + 1,s[1]))
        if s[0] - 1 >= 0 and A[s[0] - 1][s[1]] == color:
            stack.append((s[0] - 1,s[1]))
        if s[1] + 1 < len(A[0]) and A[s[0]][s[1] + 1] == color:
            stack.append((s[0],s[1] + 1))
        if s[1] - 1 >= 0 and A[s[0]][s[1] - 1] == color:
            stack.append((s[0],s[1] - 1))
            
          
def solution(A):
    N = len(A)
    M = len(A[0])
    count = 0
    for row in range(N):
        for col in range(M):
            if A[row][col] != None:
                count += 1
                visit(A, row, col)
    return count


def test():
    A = [[5,4,4],
         [4,3,4],
         [3,2,4],
         [2,2,2],
         [3,3,4],
         [1,4,4]]

    for row in A:
        print(row)

    print(solution(A))

    
test()
        
        

