

class Solution:
    def findPeakElement(self, nums: [int]) -> int:

        # 이분 탐색에서... 1개일 경우 고려하기!!
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums)-1


        while start <= end:
            mid = (start+ end) // 2
            value = nums[mid]

            # peak
            if mid == 0:
                if value > nums[mid+1]:
                    return mid
            if mid == len(nums)-1:
                if value > nums[mid-1]:
                    return mid

            if  nums[mid-1] < value and nums[mid+1] < value:
                return mid

            if value < nums[mid+1]:
                start = mid + 1
                continue

            if value < nums[mid-1]:
                end = mid -1
                continue


a = Solution()
nums = [1]
print(a.findPeakElement(nums))