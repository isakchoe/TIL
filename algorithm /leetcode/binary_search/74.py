

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n -1

        while start <= end:
            mid = (start+end)// 2

            mid_r = (mid) // n
            mid_c = (mid)% n

            mid_value = matrix[mid_r][mid_c]

            if mid_value == target:
                return True

            if mid_value > target:
                end = mid -1

            else:
                start = mid + 1

        return False

a = Solution()
matrix = [[1,1]]
target = 2
print(a.searchMatrix(matrix, target))