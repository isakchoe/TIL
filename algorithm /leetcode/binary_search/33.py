

# help from gpt
class Solution:
    def search(self, nums: [int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            temp = nums[mid]

            if temp == target:
                return mid

            # left sorted
            # 등호 -->  s, mid 같을 수 있다.
            if nums[start] <= nums[mid]:
                # 등호 없는 이유 => 같으면, 이미 위에서 타겟 찾음..
                if nums[start] <= target < nums[mid]: # 핵심 로직...
                    end = mid -1
                else:
                    start = mid + 1

            # right sorted
            else:
                # end, mid 같을 수 있다..
                if temp < target <= nums[end]:  # 핵심로직..
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


a = Solution()
nums = [5,1,3]
target = 3
print(a.search(nums,target))