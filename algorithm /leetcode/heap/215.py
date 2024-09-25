
import heapq

class Solution:
    def findKthLargest(self, nums:[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
