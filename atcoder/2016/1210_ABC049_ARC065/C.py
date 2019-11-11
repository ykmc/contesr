# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input().rstrip()
S = S[::-1]

words = ["dream","dreamer","erase","eraser"]
for i in range(4):
    words[i] = words[i][::-1]

i = 0
while i < len(S):
    for w in words:
        l = len(w)
        if w == S[i:i+l]:
            i += l
            break
    else:
        print("NO")
        sys.exit()

print("YES")