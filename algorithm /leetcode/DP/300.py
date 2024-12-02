

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        n = len(nums)

        # dp[i] = nums[i:] 값
        dp = [1] * n
        temp_min = nums[-1]

        for i in range(n-2, -1, -1):
            now = nums[i]

            # 본인 포함..
            if now < temp_min:
                dp[i] = dp[i+1] + 1
                temp_min = now

            else:
                # 본인 포함 or 본인 안포함
                temp = self.get_seq(nums[i:])
                dp[i] = max(dp[i+1], )

        print(dp)
        return dp[0]

    def get_seq(self, nums):
        count = 1
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                start = nums[i]
        return count


a = Solution()
nums = [1,3,6,7,9,4,10,5,6]
print(a.lengthOfLIS(nums))