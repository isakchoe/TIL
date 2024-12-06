

class Solution:
    # helped from gpt
    def trap(self, height: [int]) -> int:
        left, right = 0, len(height)-1
        left_max, right_max = 0 , 0

        total = 0

        while left <= right:
            # 오른쪽이 큰 경우 -> 왼쪽 만큼.. 담긴다.
            if height[left] <= height[right]:
                if height[left] <= left_max:
                    total += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1

            # 왼쪽이 큰 경우 -> 오른쪽이 기준
            else:
                if height[right] <= right_max:
                    total += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return total

a = Solution()
height =[0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(height))


