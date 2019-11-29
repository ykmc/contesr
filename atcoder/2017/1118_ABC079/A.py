# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = input().rstrip()

print("Yes" if N[0]==N[1]==N[2] or N[1]==N[2]==N[3] else "No")