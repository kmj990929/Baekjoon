#baekjoon 6603 로또 python3

from itertools import combinations

while True:
  test = input()
  if test == "0":
    break
  test = list(map(int, test.split()))[1:]
  for i in list(combinations(test,6)):
    print(" ".join(map(str,i)))
  print()

