#baekjoon 1013 contact python3

# pattern = (100+1+ | 01)+
# 조금 더 깔끔한 풀이를 생각해보자

n = int(input())

def match(target):
  if len(target) < 2:
    return False, ""

  if target.startswith('1'):
    if len(target) > 3 and target[:3] == "100":
      i = 3
      while target[i] == '0':
        i += 1
        if len(target) <= i:
          return False, ""
      while target[i] == '1':
        i += 1
        if len(target) <= i:
          return True, ""
      
      if i == len(target)-1:
        return False, ""

      if target[i+1] == "0":
        if target[i-2] == "0":
          return False, ""
        return True, target[i-1:]
      else:
        return True, target[i:]
    
    else:
      return False, ""

  else:
    if target[:2] == "01":
      return True, target[2:]
    else:
      return False, ""

for _ in range(n):
  target = input()
  result = True
  while result and target != "":
    result, target = match(target)
  
  if result:
    print("YES")
  else:
    print("NO")