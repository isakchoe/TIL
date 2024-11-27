

class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        updated = []

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.is_updated(i,j, m, n, board):
                    updated.append([i,j])


        for r,c in updated:
            temp = board[r][c]

            if temp == 1:
                board[r][c] = 0
            else:
                board[r][c] = 1

        print(board)


    def is_updated(self, row, col, m, n, matrix):
        temp = matrix[row][col]

        live = 0

        for i in range(row-1, row+2):
            for j in range(col-1, col + 2):
                if i < 0 or i >=m or j < 0 or j >= n:
                    continue

                if i == row and j == col:
                    continue

                if matrix[i][j] == 1:
                    live += 1

        if temp == 1:
            if live != 2 and live !=3:
                return True
        else:
            if live == 3:
                return True


a = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(a.gameOfLife(board))