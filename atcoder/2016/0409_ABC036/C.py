# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
A = [int(input()) for _ in range(N)]

sa = set(A)
la = sorted(sa)

ma = {x:i for i, x in enumerate(la)}

for a in A:
    print(ma[a])