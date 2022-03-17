#baekjoon 1991 트리 순회 python3

n = int(input())
nodes = dict()

class Node():
  def __init__(self, left, right):
    self.left = left if left!='.' else None
    self.right = right if right!='.' else None
    
for _ in range(n):
  a,b,c = input().split()
  node = Node(b,c)
  nodes[a] = node

def preorder(root):
  # 루트 왼 오
  print(root, end="")
  if nodes[root].left:
    preorder(nodes[root].left)
  if nodes[root].right:
    preorder(nodes[root].right)

def inorder(root):
  # 왼 루트 오
  if nodes[root].left:
    inorder(nodes[root].left)
  print(root, end="")
  if nodes[root].right:
    inorder(nodes[root].right)

def postorder(root):
  # 왼 오 루트
  if nodes[root].left:
    postorder(nodes[root].left)
  if nodes[root].right:
    postorder(nodes[root].right)
  print(root, end="")
  pass
  
preorder('A')
print()
inorder('A')
print()
postorder('A')