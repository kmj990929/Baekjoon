#baekjoon 1874 스택 수열 python3


n = int(input())

stack = []
lst = []
num = 1
def stack_add():
  global num
  while(num <= current):
    stack.append(num)
    num += 1
    lst.append("+")
  stack.pop()
  lst.append("-")

for i in range(n):
  current = int(input())
  if(len(stack) == 0):
    stack_add()
  elif(stack[-1] > current):
    lst.append("NO")
    break
  elif(stack[-1] == current):
    stack.pop()
    lst.append("-")
  else:
    stack_add()

if("NO" in lst):
  print("NO")
else:
  for j in range(len(lst)):
    print(lst[j])
