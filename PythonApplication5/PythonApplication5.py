def solution(A, K):
    array_len = len(A)
    if(array_len == 0):
        return A
    K%= array_len
    if (K == 0):
       return A
    A = A[array_len - K:] + A[:array_len - K]
    return A
print(solution([], 2))
