
def solution(S):
    S = list(S)
    if len(S) < 2:
        return ''.join(S)
    i = 0
    while i < (len(S) - 2):
        if ''.join(S[i:i+3]) == "abb":
            S[i:i+3] = "baa"
            if i >= 2:
                if ''.join(S[i-2:i+1]) == "abb":
                    i = i - 3
            else:
                i += 1
        i += 1
                
    return ''.join(S)


print(solution("abb"))
print(solution("ababb"))
print(solution("abbbabb"))
