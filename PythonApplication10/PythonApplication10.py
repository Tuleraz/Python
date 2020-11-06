def solution(S):
    L = len(S)
    if (L == 0): return -1
    if (L == 1): return 0
    A = []
    B = []
    for i in range(0, L):
        A.append(S.find(S[i], i+1, L))
    #print(A)
    for i in range(len(A)):
        if ( i+2 == A[i]):
            return B.append(A[i] - 1)
    return -1
print(solution("a"))
