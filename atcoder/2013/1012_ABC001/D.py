# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
SE = [list(input().rstrip().replace("-"," ").split()) for _ in range(N)]

A = [0]*(12*24+1)
for i in range(N):
    sh,sm = int(SE[i][0][0:2]), int(SE[i][0][2:4])
    eh,em = int(SE[i][1][0:2]), int(SE[i][1][2:4])
    sm = sm//5
    em = (em-1)//5 + 1

    si = sh*12 + sm
    ei = eh*12 + em

    A[si] += 1
    A[ei] -= 1

total = 0
for i in range(len(A)):
    # 降り始め
    if total==0 and A[i]>0:
        buf = "{0:02d}".format(i//12) + "{0:02d}".format((i%12)*5)
    # 振り終わり
    if total > 0 and total+A[i]==0:
        buf += "-" + "{0:02d}".format(i//12) + "{0:02d}".format((i%12)*5)
        print(buf)
        buf = ""
    total += A[i]