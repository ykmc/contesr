# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import Counter
N = int(input())
D = [int(input()) for _ in range(N)]

print(len(Counter(D).values()))