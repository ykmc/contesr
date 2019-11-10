# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,T = map(int,input().split())
A = list(map(int,input().split()))

lowest = 10**9+1
profit = 0
ans = 0

for a in A:
    lowest = min(lowest, a)
    if a - lowest == profit:
        ans += 1
    elif a - lowest > profit:
        profit = a - lowest
        ans = 1

print(ans)

