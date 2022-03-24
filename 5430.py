#baekjoon 5430 AC python3

from collections import deque

t = int(input())

for _ in range(t):
  p = input()
  n = int(input())
  s = input()
  if len(s) == 2:
    lst = []
  else:
    lst = list(s[1:-1].split(","))
  queue = deque(lst)

  reversed = False
  
  for ft in p:
    if ft == "R":
      if reversed:
        reversed = False
      else:
        reversed = True

    else:
      if n == 0:
        print("error")
        break
      elif reversed:
        queue.pop()
      else:
        queue.popleft()
      n -= 1
  else:
    if reversed:
      result = list(queue)[::-1]
    else:
      result = list(queue)

    result = ",".join(result)
    print("["+result+"]")
  
  
