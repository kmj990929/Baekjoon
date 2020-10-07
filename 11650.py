#baekjoon 11650 좌표 정렬하기 python3

import sys

num = int(input())

lst = []
for i in range(num):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  lst.append((a,b))

lst = sorted(lst)
for t in lst:
  print(t[0], t[1])
