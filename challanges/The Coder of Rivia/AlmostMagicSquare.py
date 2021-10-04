
def min_index(a):
    if a[0] == a[1] == a[2]:
        return -1
    index = 0
    for i in range(1, len(a)):
        if a[i] < a[index]:
            index = i
    return index

def check_sums(row_sums, col_sums):
    return row_sums[0] == row_sums[1] == row_sums[2] == col_sums[0] \
        == col_sums[1] == col_sums[2]

def get_rows_sums(A):
    return [sum(A[0:3]),sum(A[3:6]),sum(A[6:9])]

def get_columns_sums(A):
    return [sum(A[::3]), sum(A[1::3]), sum(A[2::3])]

def solution(A):
    row_sums = get_rows_sums(A)
    col_sums = get_columns_sums(A)
    stop = check_sums(row_sums, col_sums)
    M = max(row_sums + col_sums)
    while not stop:
        min_row = min_index(row_sums)
        min_col = min_index(col_sums)
        A[min_row*3 + min_col] += M - max(row_sums[min_row],col_sums[min_col])     
        row_sums = get_rows_sums(A)
        col_sums = get_columns_sums(A)
        stop = check_sums(row_sums, col_sums)
    return A
        
def test():        
    print(solution([1, 2, 3, 1, 7, 15, 2, 3, 1]))
    print(solution([0, 2, 3, 4, 1, 1, 1, 3, 1]))
    print(solution([3, 1, 20, 2, 150, 1, 2, 2, 1]))

