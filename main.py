import time
N, K  = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
start_time = time.time()
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
end_time = time.time()
print(end_time - start_time)
print(sum(A))