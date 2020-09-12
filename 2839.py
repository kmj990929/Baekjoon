#baekjoon 2839 설탕배달 python3

total = int(input())

n = total // 5
while (n >= 0):
  if((total-n*5) % 3 == 0):
    print(n+(total-n*5)//3)
    break
  else:
    n -= 1
else:
  print(-1)
