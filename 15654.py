#baekjoon 15652 N과 M(5) python3

n,m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

s = []

def dfs():
  if len(s)==m:
    print(" ".join(map(str,s)))

  for number in numbers:
    if len(s) < m and number not in s:
      s.append(number)
      dfs()
      s.pop()

dfs()