# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = int(input())
A = list(map(int,input().split()))

ans = 1
cnt = [3]+[0]*(N)

for i in range(N):
    ans *= cnt[A[i]]
    ans %= mod
    cnt[A[i]] -= 1
    cnt[A[i]+1] += 1

print(ans)