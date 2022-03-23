#baekjoon 1181 단어 정렬 python3

n = int(input())
words = dict()
for _ in range(n):
  s = input()
  length = len(s)
  if length in words:
    words[length].add(s)
  else:
    words[length] = {s}

for length in sorted(words.keys()):
  for word in sorted(list(words[length])):
    print(word)