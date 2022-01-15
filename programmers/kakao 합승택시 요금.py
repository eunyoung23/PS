# 완전탐색 문제임
INF = 2000000

def floyd(dist,n):
		for k in range(n): # 경유한 점
			for i in range(n): # 출발한 점
				for j in range(n): # 도착한 점
						if dist[i][k] + dist[k][j] < dist[i][j]:
							dist[i][j] = dist[i][k] + dist[k][j]




def solution(n,solution,a,b,fares):
	dist = [[INF for _ in range(n)] for _ in range(n)]

	#자기자신은 비용이 없음
	for i in range(n):
			dist[i][i]=0
	
	for edge in fares:
			dist[edge[0]-1][edge[1]-1] = edge[2]
			dist[edge[1]-1][edge[0]-1] = edge[2]

	floyd(dist,n)

	s -= 1
	a -= 1
	b -= 1
	answer = INF
	for k in range(n): #여기서 말하는 k는 경유지
		answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
	

	
	return answer
