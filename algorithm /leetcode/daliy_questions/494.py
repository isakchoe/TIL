
from itertools import product

class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:

        total = sum(nums)
        if total < target:
            return 0

        answer = []

        self.dfs(nums, target, 0, nums[0], total, total -nums[0],  answer)
        self.dfs(nums, target, 0, -nums[0], total, total - nums[0], answer)

        return len(answer)

    def dfs(self, nums, target, depth, temp_sum, total_sum, left_sum,  answer):

        if depth == len(nums) -1:
            if temp_sum == target:
                answer.append(1)
            return

        # back
        if temp_sum < target:
            if left_sum + temp_sum < target:
                return
        else:
            if temp_sum - left_sum > target:
                return

        # plus
        self.dfs(nums, target, depth+1, temp_sum +nums[depth+1], total_sum, left_sum - nums[depth+1], answer)
        # minus
        self.dfs(nums, target, depth + 1, temp_sum - nums[depth + 1], total_sum, left_sum - nums[depth + 1], answer)



    def findTargetSumWays2(self, nums: [int], target: int) -> int:

        if sum(nums) < target:
            return 0

        op_list =  [ [num, -num] for num in nums ]
        result = list(product(*op_list))

        answer = 0
        for r in result:
            if sum(r) == target:
                answer += 1

        return answer



a = Solution()
nums = [1,1,1,1,1]
target = 3
print(a.findTargetSumWays(nums, target))