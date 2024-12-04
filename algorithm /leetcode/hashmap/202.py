
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        dic[n] = True

        while True:
            temp = self.calculate(str(n))
            if temp == 1:
                return True

            if temp not in dic:
                dic[temp] = True
            else:
                return False

            n = temp

    def calculate(self, string_n):
        answer = 0
        for s in string_n:
            temp = int(s) ** 2
            answer += temp
        return answer

a = Solution()
n = 19
print(a.isHappy(n))
