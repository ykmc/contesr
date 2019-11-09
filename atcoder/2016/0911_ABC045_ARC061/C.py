# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,A = map(int,input().split())
X = [0] + list(map(int,input().split())) # 1枚も選ばないことに対応する 0 を先頭に追加しておく

# dp[n][k][d] : n枚からk枚選んで合計dにする選び方
dp = [[[0 for _ in range(50*N+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for n in range(N+1):
    for k in range(n+1):
        for d in range(50*k+1):
            # 選んだ数がn枚目のカードより小さい場合, そのカードは使えない
            if d < X[n]:
                dp[n][k][d] = dp[n-1][k][d]
            # そうでない場合
            else:
                # k==0のときはカードを選べないことに注意
                if k >= 1:
                    dp[n][k][d] = dp[n-1][k][d] + dp[n-1][k-1][d-X[n]]

ans = 0
for i in range(1,N+1):
    # N枚からi枚選んで平均がA,つまり合計がA*i
    ans += dp[N][i][A*i]

print(ans)