#baekjoon 1463 1로 만들기 python3

n = int(input())
dp_table = [0]*(n+1)

for i in range(2, n+1):
  dp_table[i] = dp_table[i-1]+1
  if i%2==0:
    dp_table[i] = min(dp_table[i], dp_table[i//2]+1)
  if i%3==0:
    dp_table[i] = min(dp_table[i], dp_table[i//3]+1)

print(dp_table[n])