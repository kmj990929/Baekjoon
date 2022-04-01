#baekjoon 1260 팰린드롬수 python3

while True:
  tmp = input()
  if tmp == "0":
    break

  if len(tmp)%2==0:
    if tmp[:len(tmp)//2] == tmp[len(tmp)//2:][::-1]:
      print("yes")
    else:
      print("no")
  else:
    if tmp[:len(tmp)//2] == tmp[len(tmp)//2+1:][::-1]:
      print("yes")
    else:
      print("no")
