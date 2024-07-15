

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

            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]

                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue

                if grid[nr][nc] == "1":
                    grid[nr][nc] = 0
                    q.append([nr, nc])



    def numIslands(self, grid: [str]) -> int:
        row = len(grid)
        col = len(grid[0])

        q = deque()

        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    answer += 1
                    self.bfs(grid, i, j)

        return answer


c = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(c.numIslands(grid))




