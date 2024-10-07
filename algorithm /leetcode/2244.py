
class Solution:
    def minimumRounds(self, tasks: [int]) -> int:
        dic = {}

        # 같은 숫자 개수 세기
        for num in tasks:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        answer = 0
        for k, v in dic.items():
            if v == 0 or v == 1:
                return -1

            # dp 규칙...
            if v % 3 == 0:
                answer += v // 3
            else:
                answer += v // 3 +1

        return answer


a = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]
print(a.minimumRounds(tasks))


