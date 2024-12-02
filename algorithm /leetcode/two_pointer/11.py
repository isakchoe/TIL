

class Solution:
    def maxArea(self, height: [int]) -> int:
        start = 0
        end = len(height) - 1

        answer = -1

        while start <= end:
            s_h = height[start]
            e_h = height[end]

            temp = (end - start) * min(s_h, e_h)
            answer = max(answer, temp)

            if s_h > e_h:
                end -= 1
            else:
                start += 1
        return answer

a = Solution()
height = [1,1]
print(a.maxArea(height))