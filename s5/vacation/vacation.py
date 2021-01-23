N= int(input())
a = [0]*N
b = [0]*N
c = [0]*N
for i in range(N):
    a[i], b[i], c[i] = [int(e) for e in input().split()] 
dp = [[0]*3 for i in range(N)]
def main():
    for i in range(N):
        if i ==0:
            dp[i][0] = a[i]
            dp[i][1] = b[i]
            dp[i][2] = c[i]
        else:
            dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + a[i]
            dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + b[i]
            dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + c[i]
    ans = max(dp[N-1][0], dp[N-1][1], dp[N-1][2])
    print(ans)
    
main()