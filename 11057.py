#baekjoon 11057 오르막 수 python3

n = int(input())
last_num = [1]*10

for _ in range(2,n+1):
  new_last_num = [0]*10
  for i in range(10):
    new_last_num[i] = sum(last_num[:i+1])

  last_num = new_last_num

print(sum(last_num)%10007)