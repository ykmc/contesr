# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import defaultdict
from collections import Counter
H,W,N = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

dic = defaultdict(int)
for a,b in AB:
    for dh in range(3):
        for dw in range(3):
            if 0 < a-dh <= H-2 and 0 < b-dw <= W-2:
                dic[(a-dh,b-dw)] += 1

Ans = Counter(dic.values())
Ans[0] = (H-2)*(W-2) - sum(Ans.values())

for i in range(10):
    print(Ans[i])