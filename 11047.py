#baekjoon 11047 동전0 python3


n, k = map(int,input().split())

coin_types = []
for i in range(n):
  coin_types.append(int(input()))

num = 0
cursor = n-1
while(cursor >= 0):
  if(coin_types[cursor] <= k):
    num += k // coin_types[cursor]
    k %= coin_types[cursor]
  cursor -= 1

print(num)

#commit