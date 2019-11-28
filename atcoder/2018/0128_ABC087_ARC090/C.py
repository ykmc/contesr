# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans = max(ans, sum(A1[0:i+1])+sum(A2[i:]))

print(ans)