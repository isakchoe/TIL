import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        answer = 0
        heapq.heapify(nums)
        n = len(nums)

        if nums[0] >= k:
            return answer

        for _ in range(n):
            if len(nums) < 2:
                break

            # operation
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)

            temp = min(a, b) * 2 + max(a, b)
            heapq.heappush(nums, temp)
            answer += 1

            #  check
            first = nums[0]

            if first >= k:
                break
        return answer




