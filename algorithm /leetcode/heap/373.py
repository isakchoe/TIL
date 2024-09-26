
import heapq


#  오늘의집 코테에서 나왔던 비슷한 유형
#  정렬의 특성을 이용하는 문제..


class Solution:
    def kSmallestPairs(self, nums1: [int], nums2: [int], k: int) -> [int]:
        q = []

        for i in range(min(len(nums2), k)):
            heapq.heappush(q, [nums1[0] + nums2[i], 0, i])

        answer = []

        while q and len(answer) < k:
            total, n1_idx, n2_idx = heapq.heappop(q)

            answer.append([nums1[n1_idx], nums2[n2_idx]])

            if n1_idx + 1 < len(nums1):
                heapq.heappush(q, [nums1[n1_idx+1] + nums2[n2_idx], n1_idx+1, n2_idx])

        return answer





