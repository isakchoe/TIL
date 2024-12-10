
class Solution:
    def findMin(self, nums: [int]) -> int:
        start = 0
        end = len(nums) -1

        answer = 5001
        while start <= end:

            if  0 > start or start > len(nums)-1 or end < 0 or end > len(nums)-1:
                break

            mid = (start + end) // 2

            if nums[start] < nums[end]:
                #  3, 5, 7
                if nums[start] <= nums[mid]:
                    answer = min(answer, nums[start])
                    end = mid -1
                else:
                    # 3 ,1, , 7
                    answer = min(answer, nums[mid])
                    start = mid -1
            else:
                #  6,  7 ,  3,
                if nums[start] <= nums[mid]:
                    start = mid +1
                    answer = min(answer, nums[end])
                else:
                    #  6 ,  2 ,  3
                    answer = min(answer, nums[mid])
                    end = mid -1
        return answer


a = Solution()
nums = [3,5]
print(a.findMin(nums))