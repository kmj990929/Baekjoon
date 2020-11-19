#baekjoon 2150 Strongly Connetec Component python3

#input = sys.stdin.readline생각해보기
import sys
sys.setrecursionlimit(10**9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

edge = []

for _ in range(m):
  a,b = map(int, input().split())
  edge.append(a)
  edge.append(b)

i=0
while i < m*2:
    v = edge[i]
    w = edge[i+1]
    graph[v].append(w)
    reverse_graph[w].append(v)
    i += 2

visited = [0] * (n+1) # 0:unvisited, 1:visited
visited[0] = 2
reverse_order = []

def topological_order(graph, v, visited, result):
    visited[v] = 1
    while len(graph[v]) != 0:
        node = graph[v].pop()
        #이거 생각해보자. cycle이 있을 때!
        if visited[node] == 0:
            topological_order(graph,node,visited,result)
    visited[v] = 2
    
    if not v in result:
        result.append(v)
    return result
        
while 0 in visited:
    idx = visited.index(0)
    reverse_order = topological_order(graph,idx,visited,reverse_order)

reverse_order.reverse()


new_visited = [0] * (n+1) # 0:unvisited, 1:visited

result = []
for element in reverse_order:
    if new_visited[element] == 0:
        new_result = []
        new_result = topological_order(reverse_graph, element, new_visited, new_result)
        result.append(new_result)

#출력
scc_num = len(result)
print(scc_num)

sorted_result = []
for scc in result:
  scc = sorted(scc)
  sorted_result.append(scc)


sorted_result = sorted(sorted_result, key = lambda sorted_result:sorted_result[0])

for scc in sorted_result:
  for s in scc:
    print(s, end = " ")
  print(-1)
