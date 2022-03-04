#baekjoon 2293 동전1 python3

n,k = map(int, input().split())

coin_set = [int(input()) for i in range(n)]

dp = [0]*(k+1)
dp[0] = 1 #0원을 만들 수 있는 가짓수

for coin in coin_set:
  for i in range(coin, k+1):
    if i>=coin:
      cases = dp[i-coin]
      dp[i] += cases

print(dp[k])