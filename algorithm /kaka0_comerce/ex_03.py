import heapq

INF = int(1e9)


def solution(n, passgener, train):


  def dj():
    q = []
    heapq.heappush(q, (passgener[0], 1))
    distance[1] = passgener[0]

    while q:
      dist, now = heapq.heappop(q)

      if distance[now] < dist:
        continue
    
      for i in graph[now]:
        cost = dist + i[1]

        if cost < distance[i[0]]:

          distance[i[0]] = cost
          heapq.heappush(q, (cost, i[0]))





  graph = [[] for _ in range(n+1)]
  distance = [INF]*(n+1)


  # 다익스트라 형식으로 바꿔주기 a - b 간 거리 는 c == b의 이용객 수 
  for i in train:
    graph[i[0]].append((i[1],passgener[i[1]-1]))


  dj()

  max_index = -1
  max_result = 0

  for i in range(1, n+1):
    if distance[i] >= max_result:
      max_result = distance[i]
      max_index = i
  
  print(distance)

  print([max_index, max_result])







n = 4
passgener = [2,1,2,2]
train = [[1,2], [1,3], [2,4]]


solution(n, passgener, train)