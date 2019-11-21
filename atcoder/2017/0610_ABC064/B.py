# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]

Ans = [0]*N
for a,b in AB:
    Ans[a-1] += 1
    Ans[b-1] += 1

for ans in Ans:
    print(ans)