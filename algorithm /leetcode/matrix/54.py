

class Solution:
    def spiralOrder(self, matrix):
        result = []

        # Define the boundaries of the spiral
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            #  --> 방향  (무조건 top 일 때만,)
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # down (무조건 right 일 때만, )
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left

            if top <= bottom:
                #  <-- 방향
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move the bottom boundary up

            if left <= right:
                # up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right

        return result



a = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a.spiralOrder(matrix))
