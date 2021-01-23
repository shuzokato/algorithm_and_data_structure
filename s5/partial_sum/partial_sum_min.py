N = int(input())
a = [int(e) for e in input().split()]
A = int(input())
INF = float('inf')
dp = [[INF]*25 for i in range(N)]
dp[0][0] = 0

for i in range(N-1):
    for j in range(A+1):
        dp[i+1][j] = dp[i][j]
        if j >= a[i]:
            dp[i+1][j] = min(dp[i][j-a[i]]+1,dp[i][j])
            
if dp[N-1][A] < INF:
    print(dp[N-1][A])
else:
    print(-1)