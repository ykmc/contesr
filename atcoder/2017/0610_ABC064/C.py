# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N,K = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

Cnt = [0]*(10**5+1)
for a,b in AB:
    Cnt[a] += b

i = 1
for ci in range(len(Cnt)):
    if i <= K < i+Cnt[ci]:
        print(ci)
        sys.exit()
    else:
        i += Cnt[ci]