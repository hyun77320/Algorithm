from collections import deque

n = int(input())
connect = int(input())
graph = [[] for i in range(n+1)]  
visited = [False] * (n+1)
cnt = 0

for i in range(connect):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v):
    global cnt
    queue = deque([v])  

    while queue:  
        pop = queue.popleft()
        visited[pop] = True

        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)  
                cnt += 1  
    print(cnt)

bfs(graph, 1)