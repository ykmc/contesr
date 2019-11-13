# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input().rstrip()

ai = S.find("A")
zi = S.rfind("Z")

print(zi-ai+1)