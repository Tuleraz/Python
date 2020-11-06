import sys
import time
begin_time = time.time()

#def digits(n):
#    i = 0
#    while n > 0:
#        n = n//2
#        i += 1
#    return i

#get_bin = lambda x: format(x, 'b')
# print(get_bin(sys.maxsize).count)
#print(bin(-1))
#print(bin(-2147483648))
#print(bin(2147483647))
#print(bin(4294967296))
#print(bin(sys.maxsize//2 + 2))
#A = 1
#print((sys.int_info(A)))
#print(digits(sys.maxsize))
#print(len(bin(sys.maxsize))-2)
#zeros_num = 0
#for i in range(sys.maxsize, 1, -1):
#    print(bin(i))
#    if (len(bin(i)) > zeros_num): zeros_num = len(bin(i))
#print(zeros_num)

def solution(N):
    B = bin(N).split("1")
    size_B = len(B)
    max_len = 0
    if(size_B > 2):
        for i in range(1, size_B - 1, 1):
            if( max_len < len(B[i])):
               max_len = len(B[i])
    return max_len

print("ret = ", solution(1024))

print("total runtime: ", time.time() - begin_time)

#    A = bin(N)
#    print(A.count("0", 2))
#    print(A.count("00", 2))
#    print(A.count("000", 2))
#    print(A.count("0000", 2))
#    for i in range(N, 1, -1):
#        print(bin(i))
#    return_value = 0