


class Solution:
    def countBadPairs(self, nums: [int]) -> int:
        n = len(nums)
        answer = ((n-1) * n) // 2

        dic = {}

        for i in range(len(nums)):
            temp = nums[i] - i
            if temp not in dic:
                dic[temp] = 1
            else:
                dic[temp] += 1

        for k,v in dic.items():
            answer -= ((v-1)*v)//2

        return answer


a = Solution()
nums = [1,2,3,4,5]
print(a.countBadPairs(nums))

