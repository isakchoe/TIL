
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 1:
            return ["()"]
        answer = set()
        self.dfs(n, n, n, "", answer)
        return list(answer)

    def dfs(self, n, open_left, close_left,  temp_result, answer):

        # 올바르지 않은 괄호 닫기 1
        if open_left < 0 or close_left <0:
            return

        open_used = n - open_left
        close_used = n - close_left

        # 올바르지 않은 관호 닫기 2
        if open_used < close_used:
            return

        # 정답
        if len(temp_result) == 2*n:
            answer.add(temp_result)
            return

        for i in ["(", ")"]:
            t = temp_result + i  # 이게 백트래킹...
            if i == "(":
                self.dfs(n, open_left-1, close_left, t, answer)
            else:
                self.dfs(n, open_left, close_left-1, t, answer)



a = Solution()
n = 3
print(a.generateParenthesis(n))






