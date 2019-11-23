# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
A,B = input().split()

ab = int(A+B)

print("Yes" if ab == int(ab**.5)**2 else "No")