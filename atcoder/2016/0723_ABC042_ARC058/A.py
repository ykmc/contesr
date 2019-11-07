# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
ABC = list(map(int,input().split()))
print("YES" if ABC.count(5)==2 and ABC.count(7)==1 else "NO")