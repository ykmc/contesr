# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import Counter
N = int(input())
A = list(map(int,input().split()))

cnt = len(Counter(A).values())

if cnt%2==0:
    print(cnt-1)
else:
    print(cnt)