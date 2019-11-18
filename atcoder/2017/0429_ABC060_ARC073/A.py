# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
A,B,C = input().split()

print("YES" if A[-1]==B[0] and B[-1]==C[0] else "NO")