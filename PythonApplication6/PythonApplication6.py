def solution(A):
    B = sorted(A)
    min = 0
    for i in range(len(B)):
        if(B[i] > 0):
            min = B[i] + 1
            if not (min in B):
                return min  
    return 0

print(solution([156868]))