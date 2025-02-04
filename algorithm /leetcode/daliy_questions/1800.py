

class Solution:
    def maxAscendingSum(self, nums: [int]) -> int:
        answer = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                temp = nums[i:j+1]
                if self.check_asending(temp):
                    answer = max(answer, sum(temp))

        return answer

    def check_asending(self, arr):
        for i in range(1, len(arr)):
            if arr[i-1] >= arr[i]:
                return False
        return True


a = Solution()
nums = [10,20,30,5,10,50]
print(a.maxAscendingSum(nums))