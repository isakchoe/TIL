
import copy

class Solution:
    def combine(self, n: int, k: int) -> [[int]]:

        answer = []

        self.dfs([], n, 0, k, answer)

        return list(answer)

    def dfs(self, temp, n, depth, k, answer):

        if depth == k:
            result = copy.deepcopy(temp)
            answer.append(result)
            return

        if len(temp) > 0:
            last = temp[-1]
        else:
            last = 0

        for i in range(last+1, n+1):
            temp.append(i)
            self.dfs(temp, n, depth + 1, k, answer)
            # back
            temp.pop()



a = Solution()
n = 4
k = 2
print(a.combine(n,k))