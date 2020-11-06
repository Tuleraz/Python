def solution(A):
    B = sorted(A)
    i = 0
    while( i in range(0, len(B), 1)):
        if ( i >= (len(B) - 1)) or not( B[i] == B[i+1]):
           return B[i]
        else: i+=2
    return 0

print(solution([9, 3, 9, 3, 9, 7, 9]))
