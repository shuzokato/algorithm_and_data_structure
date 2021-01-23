N = int(input())
p = [int(e) for e in input().split()]

def main():
    MAX = 10001
    dp = [0]*MAX
    dp[0] = 1
    for e in p:
        for i in reversed(range(MAX)):
            if e+i < MAX and dp[i]:
                dp[e+i] = 1

    ans = dp.count(1)

    print(ans)

main()