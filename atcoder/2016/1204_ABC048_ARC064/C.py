# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,X = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
if A[0] > X:
    ans = A[0]-X
    A[0] = X

for i in range(1,N):
    if A[i]+A[i-1] > X:
        s = A[i]+A[i-1] - X
        ans += s
        A[i] -= s

print(ans)
