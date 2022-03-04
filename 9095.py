#baekjoon 9095 1,2,3 더하기 python3

# input
n = int(input())

###
for _ in range(n):
  _input = int(input())
  dp_table = {1:1, 2:2, 3:4}
  for i in range(4,_input+1):
    dp_table[i] = dp_table[i-1]+dp_table[i-2]+dp_table[i-3]
  print(dp_table[_input])
