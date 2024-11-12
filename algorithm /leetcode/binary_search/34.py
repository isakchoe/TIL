
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1,-1]

        start_answer = len(nums) + 1
        end_answer = -1

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start+end) // 2
            temp = nums[mid]

            if temp == target:
                end_answer = max(end_answer, mid)
                start = mid +1

            elif temp > target:
                end = mid - 1
            else:
                start = mid + 1


        start2 = 0
        end2 = len(nums)-1

        while start2 <= end2:
            mid = (start2 + end2) // 2
            temp = nums[mid]

            if temp == target:
                start_answer = min(start_answer, mid)
                end2 = mid -1

            elif temp > target:
                end2 = mid - 1
            else:
                start2 = mid + 1


        if start_answer == len(nums) +1:
            return [-1,-1]

        return [start_answer, end_answer]


a = Solution()
nums = [5,7,7,8,8,10]
target = 6
print(a.searchRange(nums, target))