N,W = [int(e) for e in input().split()]
w = [0]*N
v = [0]*N
for i in range(N):
    w[i], v[i] = [int(e) for e in input().split()]

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j >= w[i]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])



print(dp[N][W])