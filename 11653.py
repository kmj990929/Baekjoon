#baekjoon 11653 소인수분해 python3

n = int(input())

while n != 1:
  for i in range(2,n+1):
    if n%i==0:
      print(i)
      break
  n = n//i
