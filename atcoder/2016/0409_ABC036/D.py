# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# function
def dfs(vi, pi):
    fx, gx = 1,1
    for ci in E[vi]:
        if ci == pi:
            continue
        f,g = dfs(ci,vi)
        fx *= g # f(Y) = g(y1) + g(y2) + ... 
        gx *= f # g(x) = f(y1) + f(y2) + ...
        fx,gx = fx%mod,gx%mod
    ret_f = (gx + fx)%mod # f(x) = g(x) + f(Y)
    ret_g = gx
    return ret_f,ret_g

# main
N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

print(dfs(0,None)[0])