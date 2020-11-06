def solution(A):
    B = sorted(A)
    if (len(A) == 1): return 3 - A[0]
    for i in range(len(B)):
        if not((i+1) == B[i]): 
            return i+1
        if ((i+1) == len(A)):
            return B[i] + 1
    return 1

print(solution([1,2,3,4,5]))
