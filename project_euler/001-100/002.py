F = [1,1]

f0,f1,f2 = 1,1,0
for i in range(2,1000):
    f2 = f0 + f1
    F.append(f2)
    f0 = f1
    f1 = f2

    if f2 > 4000000:
        break

ans = 0
for i in range(len(F)):
    if F[i]%2==0 and F[i] <= 4000000:
        ans += F[i]

print(ans)

