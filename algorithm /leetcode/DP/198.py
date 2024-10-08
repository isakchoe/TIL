


class Solution:
    def rob(self, nums: [int]) -> int:
        # n 번째 인덱스까지일때, 최대 값
        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) >=2 :
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]







a = Solution()
nums = [1,2,3,1]
print(a.rob(nums))