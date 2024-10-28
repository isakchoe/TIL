import copy


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        answer = []
        visited = [False]*len(nums)

        self.dfs(0,len(nums), [], answer, nums, visited)
        return answer

    def dfs(self, now_depth, depth, now_permute, answer, nums, visited):

        if now_depth == depth:
            temp = copy.deepcopy(now_permute)
            answer.append(temp)
            return

        for idx, num in enumerate(nums):
            if visited[idx]:
                continue

            now_permute.append(num)
            visited[idx] = True
            self.dfs(now_depth+1, depth, now_permute, answer, nums,visited)

            visited[idx] = False
            now_permute.pop()


a = Solution()
nums = [1,2,3]
print(a.permute(nums))