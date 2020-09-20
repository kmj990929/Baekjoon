#baekjoon 9012 괄호 python3

def isvps(stack, string):
  for i in range(len(string)):
    current = string[i]
    if(current == "("):
      stack.append(current)
    else:
      if(len(stack) == 0):
        return False
      else:
        stack.pop()

  if len(stack) == 0:
    return True
  else:
    return False

n = int(input())
for j in range(n):
  stack = []
  if isvps(stack, input()):
    print("YES")
  else:
    print("NO")