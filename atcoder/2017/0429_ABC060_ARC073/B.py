# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
A,B,C = map(int,input().split())

ans = "NO"
for i in range(1,B+1):
    if (A*i)%B == C:
        ans = "YES"
        break

print(ans)