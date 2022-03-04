#baekjoon 11726 2*n 타일링 python3

n = int(input())

dp_table = {1:1, 2:2}

for i in range(3,n+1):
  dp_table[i] = dp_table[i-1]+dp_table[i-2]

print(dp_table[n]%10007)
