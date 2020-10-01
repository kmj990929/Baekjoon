#baekjoon 1003 피보나치 함수 python3

n = int(input())

result = [(1,0),(0,1)]

for i in range(n):
  x = int(input())
  length = len(result)
  if length <= x:
    for i in range(length,x+1):
      zero_num = result[i-1][0] + result[i-2][0]
      one_num = result[i-1][1] + result[i-2][1]
      result.append((zero_num,one_num))
  print(result[x][0], result[x][1])
