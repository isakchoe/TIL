

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        num_dic = {}
        n = len(nums)

        for num in nums:
            if num not in num_dic:
                num_dic[num] = 1
            else:
                num_dic[num] += 1

            if num_dic[num] > (n/2):
                return num

