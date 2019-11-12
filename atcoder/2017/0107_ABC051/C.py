# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
Sx,Sy,Tx,Ty = map(int,input().split())

dx = Tx - Sx
dy = Ty - Sy

ans1 = "U"*dy + "R"*dx
ans2 = "D"*dy + "L"*dx
ans3 = "L" + "U"*(dy+1) + "R"*(dx+1) + "D"
ans4 = "R" + "D"*(dy+1) + "L"*(dx+1) + "U"

print(ans1 + ans2 + ans3 + ans4)