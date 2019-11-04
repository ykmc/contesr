// 正の整数 n 以下のすべての素数を取得
pub fn get_primes(n: usize) -> Vec<usize> {
    let mut primes = Vec::new();
    let mut is_prime = Vec::with_capacity(n+1);
    is_prime.resize(n+1, true);
    is_prime[0] = false; is_prime[1] = false;
    for i in 2..n+1 {
        if is_prime[i] {
            primes.push(i);
            
            let mut j = 2*i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
    return primes;
}