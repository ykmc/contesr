# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input().rstrip()

if S[0]==S[-1]:
    print("Second" if len(S)%2==1 else "First")
else:
    print("First" if len(S)%2==1 else "Second")