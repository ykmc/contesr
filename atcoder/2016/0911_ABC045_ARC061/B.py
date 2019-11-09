# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import deque
Sa = input().rstrip()
Sb = input().rstrip()
Sc = input().rstrip()

S = {"a":deque(Sa), "b":deque(Sb), "c":deque(Sc)}

char = "a"
while len(S[char]) > 0:
    char = S[char].popleft()

print(char.upper())