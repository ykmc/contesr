# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
ABCD = input().rstrip()

from itertools import product
ops = list(product(["+","-"],repeat=3))

x = [0]*7
for op in ops:
    x[0::2] = ABCD
    x[1::2] = op
    exp = "".join(x)
    if eval(exp)==7:
        print(exp+"=7")
        sys.exit()