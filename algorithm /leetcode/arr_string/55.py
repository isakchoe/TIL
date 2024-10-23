


class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) == 1:
            return True
        min_distance = 1

        for idx in range(len(nums)-2, -1, -1):
            if nums[idx] < min_distance:
                min_distance += 1
            else:
                # 이 지점에서 끝까지 갈 수 있으면, 그 옆 지점까지 가야할 최소 거리 1
                min_distance = 1

            if idx == 0 and nums[0] >= min_distance:
                return True
        return False


a = Solution()
nums = [1,2,0,1]
print(a.canJump(nums))