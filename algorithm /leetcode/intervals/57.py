
class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:

        if len(intervals) == 0:
            return [newInterval]

        # 누적합 이용
        max_size = max(intervals[-1][1], newInterval[1])
        arr = [0]* (max_size+1)

        # 시작, 끝 같은 경우 처리
        same_dic = {}
        if newInterval[0] == newInterval[1]:
            same_dic[newInterval[0]] = True

        for a,b in intervals:
            arr[a] += 1
            arr[b] -= 1

            if a == b:
                same_dic[a] = True


        arr[newInterval[0]] += 1
        arr[newInterval[1]] -= 1

        for i in range(1, len(arr)):
            arr[i] += arr[i-1]

        answer = []
        start = 0


        #  0인경우 따로 빼주기...
        if arr[0] == 0:
            if 0 in same_dic:
                answer.append([0,0])
        else:
            start = 0

        for i in range(1, len(arr)):

            # 시작 지점
            if arr[i] > 0 and arr[i-1] == 0:
                start = i
            # 끝
            if arr[i] == 0 and arr[i-1] > 0:
                answer.append([start, i])
            # 시작 == 끝 특수 케이스이면서, overlap 안되는 경우
            if i in same_dic:
                if arr[i] == 0 and arr[i-1] == 0:
                    answer.append([i,i])
        return answer


a = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(a.insert(intervals, newInterval))
