
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        dic = {}

        for idx, num in enumerate(nums):
            need_num = target - num
            if need_num in dic:
                return [dic[need_num], idx]
            else:
                dic[num] = idx
