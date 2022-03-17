#baekjoon 11725 트리의 부모 찾기 python3

import sys
sys.setrecursionlimit(10**9)

n = int(input())
edges = {x:[] for x in range(1,n+1)}
nodes = [0]*(n+1)

for _ in range(n-1):
  a,b = map(int, input().split())
  if a>b:
    a,b = b,a
  edges[a].append(b)
  edges[b].append(a)

def find_child(parent):
  for child in edges[parent]:
    if nodes[child] == 0:
      nodes[child] = parent
      find_child(child)

find_child(1)

for i in range(2, n+1):
  print(nodes[i])