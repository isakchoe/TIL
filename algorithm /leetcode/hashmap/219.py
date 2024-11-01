

class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        dic = {}

        for idx, num in enumerate(nums):
            if num not in dic:
                dic[num] = idx
            else:
                before_idx = dic[num]

                if idx - before_idx <= k:
                    return True
                else:
                    dic[num] = idx

        return False


a = Solution()
nums = [1,2,3,1]
k = 3
print(a.containsNearbyDuplicate(nums, k))

