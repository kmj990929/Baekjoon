#baekjoon 10814 나이순 정렬 python3

n = int(input())

namebook = {x:[] for x in range(1,201)}
for _ in range(n):
  old, name = input().split()
  old = int(old)
  namebook[old].append(name)

for old in sorted(namebook.keys()):
  for name in namebook[old]:
    print(old, name)