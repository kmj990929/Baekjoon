#baekjoon 5052 전화번호 목록 python3

def solution(n):
  phoneDict = [input() for _ in range(n)]
  phoneDict.sort()

  for num1,num2 in zip(phoneDict,phoneDict[1:]):
    if num2.startswith(num1):
      return False
  return True
    
    
        
t = int(input())
for _ in range(t):
  n = int(input())
  if solution(n):
    print("YES")
  else:
    print("NO")