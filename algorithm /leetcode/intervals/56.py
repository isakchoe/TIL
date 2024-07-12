

class Solution:
    def merge(self, intervals: [int]) -> [int]:
        arr = [0]*10001

        answer = []
        dic = {}
        for start, end in intervals:
            if start == end:
                dic[start] = 1
                continue

            arr[start] += 1
            arr[end] -= 1

        for i in range(1, 10001):
            arr[i] += arr[i-1]

        flag = 0
        for i in range(0,10001):
            if arr[i] >= 1:
                if flag == 0:
                    answer.append([i])
                    flag += 1

            if arr[i] == 0:
                if i in dic:
                    if arr[i-1] == 0:
                        answer.append([i,i])
                        continue
                if flag == 1:
                    answer[-1].append(i)
                    flag = 0

        return answer

a = Solution()

intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]


print(a.merge(intervals))





