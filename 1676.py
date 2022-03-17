#baekjoon 1676 팩토리얼 0의 개수 python3

n = int(input())

two_cnt = 0
five_cnt = 0
for i in range(2,n+1):
  while i%2==0 or i%5==0:
    if i%2==0:
      i /= 2
      two_cnt += 1
    elif i%5==0:
      i /=5
      five_cnt += 1

print(min(two_cnt, five_cnt))