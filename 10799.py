#baekjoon 10799 쇠막대기 python3

stick = input()

num = 0
stack = []
i = 0
while i < len(stick)-1:
  cursor = stick[i]
  next_cursor = stick[i+1]
  if(cursor == '('):
    if(next_cursor == ")"):
      num += len(stack)
      i+=1
    else:
      stack.append(1)
  else:
    num += stack.pop()
  i += 1

#out of index 따로 처리. else인 경우 마지막에 레이저 위치(맨 마지막은 항상 닫는 괄호이므로)
if(stick[len(stick)-2]==")"):
  num += 1

print(num)
    
