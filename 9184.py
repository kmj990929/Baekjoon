#baekjoon 9184 신나는 함수 실행 python3

dp = {}

def w(a,b,c):
  global dp
  if (a,b,c) in dp:
    return dp[(a,b,c)]
  if min(a,b,c)<=0:
    answer = 1
    dp[(a,b,c)] = answer
    return answer
  if max(a,b,c)>20:
    answer = w(20,20,20)
    dp[(a,b,c)] = answer
    return answer
  if a<b and b<c:
    answer =  w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    dp[(a,b,c)] = answer
    return answer
  else:
    answer = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    dp[(a,b,c)] = answer
    return answer

while True:
  a,b,c = map(int,input().split())
  if a==-1 and b==-1 and c==-1:
    break
  answer = w(a,b,c)
  print(f"w({a}, {b}, {c}) = {answer}".format(a=a,b=b,c=c,answer=answer))