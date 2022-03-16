#baekjoon 2225 합분해 python3

n,k = map(int, input().split())

dp_table = dict()
def dp(n,k):
  if k==1 or n==0:
    return 1
  elif (n,k) in dp_table:
    return dp_table[(n,k)]

  cnt = 0
  for i in range(n+1):
    cnt += dp(i,k-1)
  dp_table[(n,k)] = cnt
  return cnt

print(dp(n,k)%1000000000)