def bfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 1:
            graph[nx][ny] += 1
            bfs(nx, ny)

    print(graph[n -1][m - 1])


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

bfs(0,0)