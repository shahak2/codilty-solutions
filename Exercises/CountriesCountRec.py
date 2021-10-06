

def visit(A, row, col):
    print(row,col)
    color = A[row][col]
    A[row][col] = None
    if col + 1 < len(A[0]):
        if color == A[row][col + 1]:
            visit(A, row, col + 1)
    if col - 1 >= 0:
        if color == A[row][col - 1]:
            visit(A, row, col - 1)
    if row + 1 < len(A):
        if color == A[row + 1][col]:
            visit(A, row + 1, col)
    if row - 1 >= 0:
        if color == A[row - 1][col]:
            visit(A, row - 1, col)
            

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
         [1,4,4],
         [4,1,1]]

    for row in A:
        print(row)

    print(solution(A))

    
test()
        
        

