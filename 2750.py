#baekjoon 2750 수 정렬하기 python3


n = int(input())

lst = []
for i in range(n):
  lst.append(int(input()))

lst.sort()

for a in lst:
  print(a)