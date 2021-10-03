def solution(X, Y, D):
    res = (Y - X)//D
    return res if (res*D + X) >= Y else res + 1

def test():
    X = input()
    Y = input()
    D = input()
    print(solution(int(X), int(Y), int(D)))

test()
