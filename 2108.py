#baekjoon 2108 통계학 python3

import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

from collections import Counter

print(round(sum(numbers)/n))
print(numbers[n//2])

modes = []
mode_cnt = 0
for i in Counter(numbers).items():
  if mode_cnt < i[1]:
    modes = [i[0]]
    mode_cnt = i[1]
  elif mode_cnt == i[1]:
    modes.append(i[0])
if len(modes)==1:
  print(modes[0])
else:
  modes.sort()
  print(modes[1])
  
print(numbers[n-1]-numbers[0])