#baekjoon 14888 연산자 끼워넣기 python3

from itertools import permutations

n = int(input())
number = list(map(int, input().split()))
oper_num = list(map(int, input().split()))
operator = ['+']*oper_num[0] + ['-']*oper_num[1] + ['*']*oper_num[2] + ["/"]*oper_num[3]

maxsum = -10**9
minsum = 10**9
for oper in list(set(list(permutations(operator,n-1)))):
  result = number[0]
  for i in range(n-1):
    if oper[i] == "+":
      result += number[i+1]
    elif oper[i] == "-":
      result -= number[i+1]
    elif oper[i] == "*":
      result *= number[i+1]
    else:
      if result<0 and number[i+1]>0:
        result = (abs(result)//number[i+1])*-1
      else:
        result = result // number[i+1]

  if result >= maxsum:
    maxsum = result
  if result < minsum:
    minsum = result

print(maxsum)
print(minsum)
  
        
