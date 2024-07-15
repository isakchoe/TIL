

from collections import deque

class Solution:

    def bfs(self, grid, row, col,):
        q = deque()
        q.append([row,col])

        #  서, 동, 남, 북
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            r, c = q.pop()
            grid[r][c] = "1"

            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue

                if grid[nr][nc] == "O":
                    q.append([nr, nc])


    def solve(self, board: [str]) -> None:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1 :

                    if board[i][j] == "O":
                        self.bfs(board, i, j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "1":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"



c = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

print(c.solve(board))



