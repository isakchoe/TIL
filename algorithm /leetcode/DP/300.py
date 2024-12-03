

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        n = len(nums)

        #  i 번째 항목을 꼭 포함하는 연속 리스트..
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)





a = Solution()
nums = [3,5,6,2,5,4,19,5,6,7,12]
print(a.lengthOfLIS(nums))