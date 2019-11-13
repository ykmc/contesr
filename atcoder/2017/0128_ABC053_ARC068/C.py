# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
X = int(input())

print((X//11)*2 + (X%11+5)//6)