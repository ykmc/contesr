# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
S = [input().rstrip() for _ in range(N)]

for i in range(N):
    ans = []
    for j in range(N):
        ans.append(S[N-1-j][i])
    print("".join(ans))