#baekjoon 1065 한수 python3

n = int(input())

def check_num(num):
  if (num < 100):
    return num
  else:
    result = 99
    for i in range(100,num+1):
      #print("current is ",i)
      first = i % 10
      second = (i // 10) % 10
      d= first-second
      check = 0
      #print("d is ",d)
      while i >= 100:
        i = i// 10
        #print("i is ",i)
        pre = i % 10
        fo = (i//10) % 10
        if (pre-fo != d):
          #print("pre-fo is ", pre-fo)
          #print("pre is ", pre)
          #print("fo is ",fo)
          check = 1
      if (check == 0):
        result += 1
        #print("correct!")
  return result

print(check_num(n))



