# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,L = map(int,input().split())
S = list(input().rstrip() for _ in range(N))

S.sort()

print("".join(S))