

class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        start = 0
        end = arr[0]

        answer = 1

        for i in range(1, len(arr)):
            # 방향이 어디든, 작은게 start, 큰게 end
            temp_start = min(i, arr[i])
            temp_end = max(i, arr[i])

            #  겹치는 것 없음
            if temp_start > end or temp_end < start:
                answer += 1
                start = temp_start
                end = temp_end

            else:
                start = min(start, temp_start)
                end = max(end, temp_end)

        return answer


a = Solution()
arr = [3,2,1,0,4]
print(a.maxChunksToSorted(arr))





