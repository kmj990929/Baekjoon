#baekjoon 1931 회의실 배정 python3


n = int(input())

meeting_list = []
for i in range(n):
  meeting = tuple(map(int,input().split()))
  meeting_list.append(meeting)
