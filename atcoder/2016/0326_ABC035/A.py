# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
W,H = map(int,input().split())

print("4:3" if W*3==H*4 else "16:9")