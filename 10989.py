#baekjoon 10989 수 정렬하기 3 python3

import sys
input = sys.stdin.readline

n = int(input())
numbers = [0]*10001

for _ in range(n):
  now = int(input())
  numbers[now] += 1

printcnt = 0
for num, cnt in enumerate(numbers):
  if printcnt == n:
    break
  if cnt==0:
    continue
  else:
    for i in range(cnt):
      print(num)
    printcnt += cnt