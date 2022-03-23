#baekjoon 2231 분해합 python3

n = int(input())

cnt = 1
num = n
while num > 9:
  num /= 10
  cnt += 1

start = max(0,n-9*cnt)
for i in range(start,n):
  sum_i = sum(map(int, str(i)))
  if i+sum_i == n:
    print(i)
    break
else:
  print(0)