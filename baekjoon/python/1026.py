# 1026번 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

sum = 0

for i in range(N):
    sum += A[i] * B[i]

print(sum)