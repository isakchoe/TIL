

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        answer = []

        # 메모리 사용량 = > O(N)
        acc_start = [nums[0]]
        acc_end = [nums[-1]]

        for i in range(1, len(nums)):
            temp = acc_start[-1] * nums[i]
            acc_start.append(temp)

        for i in range(len(nums)-2, -1, -1):
            temp = acc_end[-1] * nums[i]
            acc_end.append(temp)

        # 누적합, 정순과 역순을 이용함..
        acc_end.reverse()
        answer.append(acc_end[1])
        n = len(acc_start)-2

        for i in range(n):
            temp = acc_start[i] * acc_end[i+2]
            answer.append(temp)

        answer.append(acc_start[-2])
        return answer







a = Solution()
nums = [-1,1,0,-3,3]
print(a.productExceptSelf(nums))