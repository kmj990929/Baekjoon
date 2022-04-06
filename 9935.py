#baekjoon 9935 문자열 폭발 python3

import re

target = input()
bomb = list(input())
_bomb = bomb[:-1]

stack = []
cursor = 0
for alpha in target:
  if alpha == bomb[-1]:
    if len(stack)>=len(bomb)-1-cursor and stack[-(len(bomb)-1-cursor):cursor]==_bomb:
      cursor -= (len(bomb)-1)
    else:
      if cursor == len(stack):
        stack.append(alpha)
      else:
        stack[cursor] = alpha
      cursor += 1
  else:
    if cursor == len(stack):
      stack.append(alpha)
    else:
      stack[cursor] = alpha
    cursor += 1

result = "".join(stack[:cursor])
if result:
  print(result)
else:
  print("FRULA")