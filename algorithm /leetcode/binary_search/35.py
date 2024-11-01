
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2

            temp = nums[mid]

            if temp == target:
                return mid

            if temp > target:
                end = mid-1
                continue

            if temp < target:
                start = mid+1
                continue
        return start

a = Solution()
nums = [1,3]
target = 3
print(a.searchInsert(nums, target))