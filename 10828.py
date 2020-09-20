#baekjoon 10828 스택 python3


import sys
input = sys.stdin.readline
n = int(input())

class Stack(list):
  def __init__(self):
    self.lst = []
  
  def push(self,num):
    self.lst.append(num)

  def top(self):
    if(len(self.lst) == 0):
      print(-1)
    else:
      print(self.lst[-1])

  def size(self):
    return (len(self.lst))

  def empty(self):
    if(self.size() == 0):
      print(1)
    else:
      print(0)

  def pop(self):
    if(self.size() == 0):
      print(-1)
    else:
      print(self.lst.pop())

stack = Stack()
for i in range(n):
  order = input().split()
  if(order[0] == 'push'):
    stack.push(int(order[1]))
  elif(order[0] == 'top'):
    stack.top()
  elif(order[0] == "size"):
    print(stack.size())
  elif(order[0] == "empty"):
    stack.empty()
  elif(order[0] == "pop"):
    stack.pop()

