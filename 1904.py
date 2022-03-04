#baekjoon 1904 01타일 python3

n= int(input())
dp_table = [0,1,2]

for i in range(3, n+1):
  dp_table.append((dp_table[i-1] + dp_table[i-2])%15746)

print(dp_table[n])