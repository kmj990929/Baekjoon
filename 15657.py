#baekjoon 15657 N과 M(8) python3

n,m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

s = []
def dfs():
  if len(s)==m:
    print(" ".join(map(str,s)))

  for nn in numbers:
    if len(s)==0 or (len(s)<m and s[-1] <= nn):
      s.append(nn)
      dfs()
      s.pop()

dfs()