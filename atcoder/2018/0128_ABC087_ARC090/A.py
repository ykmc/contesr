# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
X = int(input())
A = int(input())
B = int(input())

print((X-A)%B)