#baekjoon 2606 바이러스 python3


n = int(input())
m = int(input())

field = [[] for _ in range(n+1)]
visited = [[False] for _ in range(n+1)]

#field 설정
for i in range(m):
  a,b = map(int, input().split())
  field[a].append(b)
  field[b].append(a)

count = 0
def dfs(field, v, visited):
  global count
  visited[v][0] = True
  for i in field[v]:
    if not visited[i][0]:
      dfs(field,i,visited)
      count += 1
  
dfs(field,1,visited)
print(count)