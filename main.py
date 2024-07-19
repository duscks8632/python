def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False
    if graph[a][b] == 0:
        graph[a][b] = 1
        dfs(a -1, b)
        dfs(a + 1,b)
        dfs(a, b - 1)
        dfs(a, b + 1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)