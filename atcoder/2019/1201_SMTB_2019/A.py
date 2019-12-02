# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
M1,D1 = map(int,input().split())
M2,D2 = map(int,input().split())

print("1" if D2==1 else "0")