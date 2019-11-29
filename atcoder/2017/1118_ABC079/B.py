# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = int(input())

num = [2,1]
for i in range(N):
    num.append(num[-2]+num[-1])

print(num[N])