#baekjoon 9663 N-Queen python3

n = int(input())
queen = [0]*n

def dfs(queen, n, row):
  cnt = 0
  
  if n==row:
    return 1

  for col in range(n):
    queen[row] = col
    for x in range(row):
      if queen[x]==queen[row]:
        break
      elif abs(queen[x]-queen[row]) == abs(x-row):
        break
    else:
      cnt += dfs(queen, n, row+1)

  return cnt

      
print(dfs(queen, n, 0))