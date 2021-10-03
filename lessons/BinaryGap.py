
def int_to_bin(N):
    st = ""
    while N > 0:
        st = str(N % 2) + st
        N = N // 2
    return st

def solution(N):
    count = 0
    current_count = 0
    bin_N = int_to_bin(N)
    flag = False
    for c in bin_N:
        if c == "0":
            if flag:
                current_count += 1                          
        if c == "1":
            if not flag:
                flag = True
            else:
                if current_count > count:
                    count = current_count
                current_count = 0
    return count
                

def test():
    x = input()
    st = int_to_bin(int(x))
    print(st)
    print(solution(int(x)))
