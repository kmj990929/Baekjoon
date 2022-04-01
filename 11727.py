#baekjoon 11727 2*n 타일링 2 python3

n = int(input())
dp_table = {1:1, 2:3}

for i in range(3,n+1):
  dp_table[i] = dp_table[i-1] + 2*dp_table[i-2]

print(dp_table[n]%10007)