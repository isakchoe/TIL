from collections import deque

#
# # 입력
# t = int(input())
#
# for _ in range(t):
#     # 편의점 수
#     cvs = int(input())
#
#     loca = []
#
#     graph = [[0]*(10000) for _ in range(10000)]
#     visited = [[False]*(10000) for _ in range(10000)]
#
#     for i in range(2+cvs):
#         x,y = map(int, input().split())
#         loca.append([x,y])
#
#     for i in range(1,len(loca)-1):
#         r, c = loca[i]
#         # 편의점
#         graph[r][c] = -1
#
#     q = deque()
#     q.append(loca[0])
#     # 방문처리
#     visited[loca[0][0]][loca[0][1]] = True
#
#     answer = 0
#
#     while q:
#         x, y = q.popleft()
#         print(graph)
#
#         if x == loca[-1][0] and y == loca[-1][1]:
#             answer += 1
#             break
#
#
#         dx = [0,0,1,-1]
#         dy = [1,-1,0,0]
#
#         for i in range(4):
#             nx = x +dx[i]
#             ny = y+ dy[i]
#
#             if 0<= nx < (10000) and 0<= ny < (10000):
#                 # 맥주 소비
#                 if graph[x][y] >= 1000:
#                     continue
#
#
#                 # 다음이 편의점이면
#                 if graph[nx][ny] == -1:
#                     if visited[nx][ny] == False:
#                         visited[nx][ny] = True
#                         # 리셋
#                         graph[nx][ny] = 0
#                         q.append([nx,ny])
#
#                 elif visited[nx][ny] == False:
#                     visited[nx][ny] = True
#                     graph[nx][ny] = graph[x][y] +1
#                     q.append([nx,ny])
#
#
#     if answer == 1:
#         print("happy")
#     else:
#         print("sad")



# -------------- 시간 초과 ---------------------

# 입력 받기
#
# t = int(input())
#
# for _ in range(t):
#     cvs = int(input())
#     graph = [[0] *10000 for _ in range(10000)]
#     visited = [[False]*10000 for _ in range(10000)]
#
#     loca = []
#
#     for i in range(cvs+2):
#         x,y = map(int, input().split())
#         loca.append([x,y])
#
#     # 시작 세팅
#     q = deque()
#     q.append(loca[0])
#
#     # 편의점 세팅
#     for i in range(1,len(loca)-1):
#         r,c = loca[i]
#         print(r,c)
#         graph[r][c] = -1
#
#     # print(graph)
#
#     index = 0
#
#     while q:
#         x,y = q.popleft()
#
#         # 목적지 도착
#         if x == loca[-1][0] and y == loca[-1][1]:
#               index = 1
#               break
#         # 더이상 전진 못함
#         if graph[x][y] == 1000:
#             continue
#
#         dx = [0,0,1,-1]
#         dy = [1,-1,0,0]
#
#         for i in range(4):
#             nx = x +dx[i]
#             ny = y + dy[i]
#
# #             범위
#             if 0<=nx<10000 and 0<=ny<10000:
#                 if visited[nx][ny] == False:
#                     # 방문처리
#                     visited[nx][ny] = True
#                     q.append([nx,ny])
# #                     편의덤이면
#                     if graph[nx][ny] == -1 :
#                         graph[nx][ny] = 0
#                     else:
#                         graph[nx][ny] = graph[x][y] + 1
#
#     if index == 1:
#         print("happy")
#     else:
#         print("sad")
#

# 플로이드 와샬

t = int(input())

for _ in range(t):
    cvs = int(input())

    loca = []
    for i in range(cvs+2):
        x,y = map(int, input().split())
        loca.append([x,y])

    INF = int(1e9)
    # 행랼,  0 ==> 출발, 마지막 ==> 도착지
    distance = [[INF]*(cvs+2) for _ in range(cvs+2)]

    for i in range(cvs+2):
        x,y = loca[i]
        for j in range(cvs+2):
            if i ==j:
                distance[i][j] = True

            if  i != j and abs(loca[j][0] - x) + abs(y - loca[j][1]) <=1000:
                distance[i][j] = True


    for k in range(cvs+2):
        for i in range(cvs+2):
            for j in range(cvs+2):
                if distance[i][k] == True and distance[k][j] == True:
                    distance[i][j] = True


    if distance[0][-1] == True:
        print("happy")
    else:
        print("sad")






