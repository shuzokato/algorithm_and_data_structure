N = int(input())
a = [int(e) for e in input().split()]
A = int(input())

dp = [[0]*25 for i in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(A+1):
        dp[i+1][j] = dp[i][j]
        if j >= a[i]:
                dp[i+1][j] += dp[i][j-a[i]]
            
print(dp[N][A])