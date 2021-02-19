
from collections import deque




def solution(board):

    l = len(board)

    q = deque()

    q.append([[0,0], [0,1]])
    #     동서남북
    dx = [0 ,0 ,1 ,-1 ,1 ,-1 ,0 ,0 ]
    dy = [1 ,-1 ,0 ,0 ,1, 1 ,0 ,0]
    ex = [0 ,0 ,1 ,-1 ,0 ,0 ,1 ,-1]
    ey = [1 ,-1 ,0 ,0 ,0 ,0 ,-1 ,-1]

    while q:
        left, right = q.popleft()

        r1 = left[0]
        c1 = left[1]

        r2 = right[0]
        c2 = right[1]

        for i in range(8):
            nr_1 = r1 + dx[i]
            nc_1 = c1 + dy[i]
            nr_2 = r2 + ex[i]
            nc_2 = c2 + ey[i]


            if nr_1 >=0 and nr_1 <l and nr_2 >= 0 and nr_2 < l and nc_1 >= 0 and nc_1 < l and nc_2 >= 0 and nc_2 < l:
                if board[nr_1][nc_1] != 1  and board[nr_2][nc_2] != 1:

                    if board[nr_1][nc_1] == 0 or board[nr_2][nc_2] == 0:

                        # 끝 행열을 두번 체크하지 않게 만들면 정답 가능
                        board[nr_1][nc_1] =  board[r1][c1] + 2
                        board[nr_2][nc_2] = board[r2][c2] + 2

                        if nr_1 == l-1 and nc_1 == l-1:
                            return (board[nr_1][nc_1]//2)

                        if nr_2 == l-1 and nc_2 == l-1:
                            return (board[nr_2][nc_2]//2)


                        q.append([[nr_1, nc_1], [nr_2, nc_2]])

    return (board[l - 1][l - 1]//2)

