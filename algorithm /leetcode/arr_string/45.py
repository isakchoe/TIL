

class Solution:
    def jump(self, nums: [int]) -> int:
        if len(nums) == 1:
            return 0

        min_dp = [10000]* (len(nums)+ 1)

        for idx in range(len(nums)-2, -1, -1):
            temp = nums[idx]

            # 직접 끝 도달
            if temp + idx >= len(nums) -1:
                min_dp[idx] = 1

            else:
                min_value = min(min_dp[idx: idx + temp+1])
                min_dp[idx] = min_value + 1
        return min_dp[0]


a = Solution()
nums = [2,3,0,1,4]
print(a.jump(nums))

