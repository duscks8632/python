from collections import deque
def bfs(graph, start, visited):
	# 1번 노드를 deque에 넣음
	queue = deque([start])
	# 1번 노드 방문처리
	visited[start] = True
	# queue가 빌때까지 반복
	while queue:
		# 큐에 있는 맨 밑 노드 뽑기
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			# 방문 안한 인접노드만 큐에 추가하기
			if not visited[i]:
				queue.append(i)
				visited[i] = True

graph = [
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)