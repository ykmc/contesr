# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import defaultdict
N = int(input())

Primes = []
is_prime = [True]*(N+1)
is_prime[0] = is_prime[1] = False

for i in range(2,N+1):
    if is_prime[i]:
        Primes.append(i)
        for j in range(i*2,N+1,i):
            is_prime[j] = False

dic = defaultdict(int)

for i in range(2,N+1):
    for p in Primes:
        while i%p==0:
            dic[p] += 1
            i //= p
        if i==1:
            break

ans = 1
mod = 10**9+7
for v in dic.values():
    ans *= v+1
    ans %= mod

print(ans)