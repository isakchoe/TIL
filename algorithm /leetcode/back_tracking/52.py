

class Solution:
    def totalNQueens(self, n: int) -> int:
        visited = [[0]*n for _ in range(n)]
        answer = []

        for i in range(n):
            self.dfs(0, i, n, visited, answer)
            # reset 해주어야 한다...
            self.remove_queen(0, i, n, visited)
        return len(answer)

    def dfs(self, row, col,  n, visited, answer):
        # put queen
        self.put_queen(row, col, n, visited)

        # 종료조건에서, 백트래킹 주의하자.
        # 방문처리하지 않고, 백트래킹하면 에러!!
        if row == n-1:
            answer.append(1)
            return

        for j in range(n):
            if visited[row+1][j] == 0:
                # put next level
                self.dfs(row+1, j, n, visited, answer)

                # back
                # 넣고, 빼고는 원자성! 유지해야 한다.
                self.remove_queen(row+1,j,n, visited)




    def put_queen(self, row, col, n, visited):
        visited[row][col] += 1

        # row
        for j in range(n):
            if j == col:
                continue
            visited[row][j] += 1
        # col
        for i in range(n):
            if i == row:
                continue
            visited[i][col] += 1

        # 북서
        t_row = row + 1
        t_col = col + 1

        while 0<= t_row < n and 0<=t_col <n:
            visited[t_row][t_col] += 1
            t_col += 1
            t_row += 1


        # 동남
        t_row2 = row -1
        t_col2 = col -1

        while 0<= t_row2 < n and 0<=t_col2 <n:
            visited[t_row2][t_col2] += 1
            t_row2 -= 1
            t_col2 -= 1

        # 남서
        t_row3 = row +1
        t_col3 = col -1

        while 0<= t_row3 < n and 0<=t_col3 <n:
            visited[t_row3][t_col3] +=1
            t_row3 += 1
            t_col3 -= 1

        # 북동
        t_row4 = row-1
        t_col4 = col+1

        while 0 <= t_row4 < n and 0 <= t_col4 < n:
            visited[t_row4][t_col4] += 1
            t_row4 -= 1
            t_col4 += 1


    # 겹치는거 빼면, 안된다!!
    def remove_queen(self, row, col, n, visited):
        visited[row][col] -= 1

        # row
        for j in range(n):
            if j == col:
                continue
            visited[row][j] -= 1
        # col
        for i in range(n):
            if i == row:
                continue
            visited[i][col] -= 1

        # 북서
        t_row = row +1
        t_col = col +1

        while 0 <= t_row < n and 0 <= t_col < n:
            visited[t_row][t_col] -= 1
            t_col += 1
            t_row += 1

        # 동남
        t_row2 = row -1
        t_col2 = col -1

        while 0 <= t_row2 < n and 0 <= t_col2 < n:
            visited[t_row2][t_col2] -= 1
            t_row2 -= 1
            t_col2 -= 1

        # 남서
        t_row3 = row +1
        t_col3 = col -1

        while 0 <= t_row3 < n and 0 <= t_col3 < n:
            visited[t_row3][t_col3] -= 1
            t_row3 += 1
            t_col3 -= 1

        # 북동
        t_row4 = row -1
        t_col4 = col +1

        while 0 <= t_row4 < n and 0 <= t_col4 < n:
            visited[t_row4][t_col4] -= 1
            t_row4 -= 1
            t_col4 += 1



a = Solution()
n = 1
print(a.totalNQueens(n))







