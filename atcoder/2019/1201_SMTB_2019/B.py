# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = int(input())

from math import ceil
if ceil(N/1.08) < (N+1)/1.08:
    print(ceil(N/1.08))
else:
    print(":(")