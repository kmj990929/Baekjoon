#baekjoon 4949 균형잡힌 세상 python3

from collections import deque

def balance(string):
  queue = deque([])
  for i in string:
    if i in ["[", "("]:
      queue.append(i)
    elif i == ")":
      if len(queue)==0:
        return False
      elif queue.pop()=="(":
        continue
      else:
        return False
    elif i == "]":
      if len(queue)==0:
        return False
      elif queue.pop()=="[":
        continue
      else:
        return False
  return len(queue)==0

while True:
  test = input()
  if test  == ".":
    break
  if balance(test):
    print("yes")
  else:
    print("no")