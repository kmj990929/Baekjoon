#baekjoon 15829 Hashing python3

r= 31
M = 1234567891

l = int(input())
alpha = input()

tmpsum = 0
for i, a in enumerate(alpha):
  ascii = ord(a)-ord("a")+1
  tmpsum += ascii*(r**i)

print(tmpsum%M)