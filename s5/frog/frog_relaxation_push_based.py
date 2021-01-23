N = int(input())
h = [int(e) for e in input().split()]
def main():
    INF = float('inf')
    dp = [INF]*N
    dp[0] = 0
    for i in range(0,N):
        if i + 1 < N:
            dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1]-h[i]))
        if i + 2 < N:
            dp[i+2] = min(dp[i+2], dp[i]+abs(h[i+2]-h[i]))
    print(dp[N-1])
        
main()