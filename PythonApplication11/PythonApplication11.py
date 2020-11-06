"""
This is a demo task.
Write a function:
def solution(A):
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
import time, random
begin_time = time.time()

def solution(A):
    if(A == []): return 1
    if(len(A) == 1):
        if(A[0] < 1): return 1
        else:
            for i in range(1,A[0] + 1):
                if not(i in A):
                    return i
    B = sorted(A)
    for i in range(0, len(B) - 1):
        if(B[i] > 0 and not(B[i]==B[i+1])):
            if not(B[i] + 1 == B[i+1]):
                return B[i] + 1
    if(B[len(B) - 1] < 0): 
        return 1
    else:
        for j in range(1, B[len(B) - 1] + 2):
            if not(j in B):
                return j



#    for i in range(len(A)):
#        if(min < A[i]): min = A[i]
#        if(min > 0):
#            for j in range(old_val[len(old_val)-1], min +1):
#                if not (j in A):
#                    return j
#                else:
#                    if(not (j in old_val)):
#                       old_val.append(j)
#    if(min > 0):
#        if(i == len(A) - 1):
#            return min + 1
#        else: 
#            return min
#    else:
#        return 1
income =[]
#income =[-1,-1,2,-1,2]
#income = [-10000000,10000001]
#random.seed(3)
#for i in range(0,100): income.append(random.randint(0, 100))
#for i in range(100,200): income.append(random.randint(102, 200))
for i in range(100000): income.append(i)
#income.append(40001)
#print(income)
print(solution(income))

print("total runtime: ", time.time() - begin_time)