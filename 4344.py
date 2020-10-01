#baekjoon 4344 평균은 넘겠지 python3

n = int(input())

for i in range(n):
  lst = list(map(int, input().split()))

  mean = sum(lst[1:])/lst[0]
  num = 0
  for j in range(1,lst[0]+1):
    if (lst[j]>mean):
      num += 1
  
  result = num / lst[0] * 100
  print(f'{result:.3f}%')