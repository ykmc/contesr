# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
H,W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]

from scipy.sparse.csgraph import floyd_warshall
D = floyd_warshall(C)

cnt = [0]*10
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            cnt[A[i][j]] += 1

ans = 0
for i in range(10):
    ans += cnt[i]*D[i][1]

print(int(ans))