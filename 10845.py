#baekjoon 10845 큐 python3

#sol1 : collections.deque 이용
"""
from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

n = int(input())
for i in range(n):
  current = input().split()
  size_queue = len(list(queue))
  if(current[0] == 'push'):
    queue.append(int(current[1]))
  elif(current[0] == 'pop'):
    if(size_queue == 0):
      print(-1)
    else:
      print(queue.popleft())
  elif(current[0] == 'size'):
    print(size_queue)
  elif(current[0] == 'empty'):
    if(size_queue == 0):
      print(1)
    else:
      print(0)
  elif(current[0] == 'front'):
    if(size_queue == 0):
      print(-1)
    else:
      print(list(queue)[0])
  elif(current[0] == 'back'):
    if(size_queue == 0):
      print(-1)
    else:
      print(list(queue)[-1])
"""

#sol2 : class 이용
import sys
input = sys.stdin.readline

class Queue(list):
  def __init__(self):
    self.lst = []
  def push(self,num):
    self.lst.append(num)
  def pop(self):
    if(len(self.lst)==0):
      return -1
    else:
      result = self.lst[0]
      self.lst = self.lst[1:]
      return result
  def size(self):
    return len(self.lst)
  def empty(self):
    if(self.size() == 0):
      return 1
    else:
      return 0
  def front(self):
    if(self.size() == 0):
      return -1
    else:
      return self.lst[0]
  def back(self):
    if(self.size() == 0):

      return -1
    else:
      return self.lst[-1]

queue = Queue()
n = int(input())
for i in range(n):
  current = input().split()
  if(current[0] == 'push'):
    queue.push(int(current[1]))
  elif(current[0] == 'pop'):
    print(queue.pop())
  elif(current[0] == 'size'):
    print(queue.size())
  elif(current[0] == 'empty'):
    print(queue.empty())
  elif(current[0] == 'front'):
    print(queue.front())
  elif(current[0] == 'back'):
    print(queue.back())