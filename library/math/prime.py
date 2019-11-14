def get_primes(n):
    primes = []
    is_prime = [False,False]+[True]*(n-1)
    for i in range(2,N+1):
        if is_prime[i]:
            primes.append(i)

            j = 2*i
            while j <= n:
                is_prime[j] = False
                j += i

    return primes