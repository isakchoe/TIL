
import  heapq
import  sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [ [] for i in range(n+1)]
distance = [INF]*(n+1)


for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

def dijstra(start):
    q =[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, node_num = heapq.heappop(q)

        if distance[node_num] < dis:
            continue

        for i in graph[node_num]:
            cost = i[1] + dis

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijstra(c)

count = 0
time = 0
for i in range(1,n+1):
    if distance[i] != INF and distance[i] != 0:
        count +=1
        time = max(time, distance[i])

print(count, time)
