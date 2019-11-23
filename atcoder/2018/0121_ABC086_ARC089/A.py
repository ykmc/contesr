# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
A,B = map(int,input().split())

print("Even" if (A*B)%2==0 else "Odd")