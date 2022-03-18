#baekjoon 2156 포도주 시식 python3

n = int(input())
wines = []
for _ in range(n):
  wines.append(int(input()))

if n == 1:
  print(wines[0])
elif n == 2:
  print(wines[0]+wines[1])
else:
  dp = [wines[0], wines[0]+wines[1], max(wines[0]+wines[2], wines[1]+wines[2], wines[0]+wines[1])]
  
  for i in range(3,n):
    pass0 = wines[i-1]+dp[i-3]
    pass1 = dp[i-2]
    if i < 4:
      pass2 = 0
    else:
      pass2 = wines[i-2]+dp[i-4] #max(dp[i-3],wines[i-2]+dp[i-4])
    dp.append(max(max(pass0,pass1,pass2)+wines[i],dp[i-1]))

  print(max(dp))

               