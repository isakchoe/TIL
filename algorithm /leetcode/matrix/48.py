
import copy

class Solution:
    def rotate(self, matrix: [int]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        original = copy.deepcopy(matrix)

        n = len(matrix)

        for i in range(n):
            for j in range(n-1, -1, -1):
                matrix[i][n-1-j] = original[j][i]

