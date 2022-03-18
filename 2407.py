#baekjoon 2407 조합 python3

n,m = map(int, input().split())

dp = [1]
for i in range(1,n+1):
  dp.append(dp[-1]*i)

answer = dp[n]//(dp[m]*dp[(n-m)])
print(answer)