#baekjoon 2178 미로 탐색 python3

from collections import deque

n,m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

visited = [[False]*m for j in range(n)]
move = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(maze, start, visited):
    global n,m

    queue = deque([start])
    x, y = start
    visited[y][x] = True
    count = 1

    while queue:
        count += 1
        for _ in range(len(queue)):
            cursor = queue.popleft()
            if cursor == (m-1, n-1):
                return count-1

            for mi in move:
                dx = cursor[0] + mi[0]
                dy = cursor[1] + mi[1]
                if dx >= 0 and dy >= 0 and dx < m and dy < n \
                    and maze[dy][dx] == 1 and visited[dy][dx] == False:
                    visited[dy][dx] = True
                    queue.append((dx,dy))

print(bfs(maze, (0,0), visited))


