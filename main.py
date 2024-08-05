from collections import deque
def bfs(x, y):
    queue = deque()
    #튜플로 한 이유: 좌표값은 변하지 않기에, append할때 하나씩만 추가 가능하기에
    queue.append((x, y))
    while queue:
        # x,y를 안 넣었음..
        # 초기값을 x,y로 뽑는다
        x, y = queue.popleft()
        #상하좌우에 대해서 유효한 값이 있는지 본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 배열 밖으로 넘어가면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue
            #  방문한 적 없고 괴물이 없는 경우
            if graph[nx][ny] == 1:
                # 이때 좌표의 값을 +1 추가해 카운트한다
                graph[nx][ny] = graph[x][y] + 1
                #리스트가 아니라 튜플
                # 큐에 추가하고 다시 추가한 걸 뽑을 수 있도록 한다.
                queue.append((nx, ny))
    #x,y는 nx, ny이 아니니 그냥 젤 마지막꺼 리턴하는 게 맞다
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input())))
# 하 우 좌 상
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

print(bfs(0, 0))
