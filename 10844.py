#baekjoon 10844 쉬운 계단수 python3

n = int(input())
last_num = [0] + [1]*9

for _ in range(2,n+1):
  new_last_num = [0]*10
  
  for j in range(10):
    if j==0:
      new_last_num[1] += last_num[0]
    elif j==9:
      new_last_num[8] += last_num[9]
    else:
      new_last_num[j-1] += last_num[j]
      new_last_num[j+1] += last_num[j]

  last_num = new_last_num

print(sum(last_num)%1000000000)