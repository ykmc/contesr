# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from math import ceil
from decimal import *
N = int(input())
TA = [list(map(int,input().split())) for _ in range(N)]


t,a = 1,1
for i in range(N):
    n = Decimal(max(ceil(t/TA[i][0]), ceil(a/TA[i][1])))
    t = n*TA[i][0]
    a = n*TA[i][1]

print(t+a)