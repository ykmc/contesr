# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,Q = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(Q)]

A = [0]*(N+1)
for l,r in LR:
    A[l-1] += 1
    A[r] -= 1

for i in range(N):
    A[i+1] += A[i]
    A[i] %= 2

print("".join(map(str,A[:N])))