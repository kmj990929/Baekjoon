#baekjoon 15649 N과 M(2) python3

n,m = map(int, input().split())

s = []
def dfs():
  if len(s)==m:
    print(" ".join(map(str,s)))
    return

  for i in range(1,n+1):
    if i not in s:
      if len(s)==0 or s[-1] < i:
        s.append(i)
        dfs()
        s.pop()

dfs()