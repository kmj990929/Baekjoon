#baekjoon 11660 구간 합 구하기 5 python3
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
table = []
dp = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
  row = list(map(int, input().split()))
  table.append(row)

for a in range(1,n+1):
  for b in range(1,n+1):
    dp[a][b] = dp[a-1][b]+dp[a][b-1]-dp[a-1][b-1]+table[a-1][b-1]

for _ in range(m):
  x1,y1,x2,y2 = map(int,input().split())
  answer = dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
  print(answer)
