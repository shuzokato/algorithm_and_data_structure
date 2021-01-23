N = int(input())
h = [int(e) for e in input().split()]
INF = float('inf')
dp = [INF]*N

def main():
    print(rec(N-1))

def rec(i):
    if dp[i] < INF:
        return dp[i]
    if i == 0:
        return 0 
    res = INF
    res = min(res, rec(i-1) + abs(h[i]-h[i-1]))
    if i > 1:
        res = min(res, rec(i-2)+abs(h[i]-h[i-2]))
    dp[i] = res
    return dp[i]

main()