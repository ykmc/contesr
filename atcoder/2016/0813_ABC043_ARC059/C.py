# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
A = list(map(int,input().split()))

ans = float("inf")
for d in range(-100,101):
    total = 0
    for i in range(N):
        total += (d-A[i])**2
    ans = min(ans,total)

print(ans)