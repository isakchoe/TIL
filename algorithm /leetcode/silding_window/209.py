
class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        start = 0
        end = 0

        total_sum = nums[0]

        answer = len(nums) +1

        while start < len(nums):
            if total_sum >= target:
                answer = min(answer, end-start+1)

                # 축소
                total_sum -= nums[start]
                start += 1

            else:
                # 종료 조건
                if end == len(nums) - 1:
                    break

                end += 1
                total_sum += nums[end]

        if answer > len(nums):
            return 0
        return answer


a = Solution()
target = 11
nums = [1,1,1,1,1,1,1,1]
print(a.minSubArrayLen(target, nums))





