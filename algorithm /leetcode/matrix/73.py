

class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        # space = O(m+n)
        row = []
        col = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        for r in row:
            matrix[r] = [0]*n

        for c in col:
            for i in range(m):
                matrix[i][c] = 0

        print(matrix)


    def setZeroes2(self, matrix: [[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        # space = O(1)
        # matrix[i][j]==0, 인 i,j 를 0행 j 열 , i행 0열에 표시하자..


        # 0 찾기
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))


        # 0 찾기
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 0 표시 - 0행, 0열 보다 선행되어야함. 안그러면 전체가 0 이 됨
        for i in range(1, m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # 0행, 0열 별개 처리..
        if first_row_zero:
            matrix[0] = [0]*n

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


        print(matrix)

a = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
a.setZeroes2(matrix)