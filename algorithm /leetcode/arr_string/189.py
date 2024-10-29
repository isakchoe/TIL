
class Solution:
    # # 2번풀이  O(N) = 3ms, chatgpt
    def rotate(self, nums: [int], k: int) -> None:

        k  %= len(nums)
        nums.reverse()

        half = k//2

        for i in range(half):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        n = len(nums)
        left_half =  (n-k)// 2

        for i in range(left_half):
            nums[i+k], nums[-(i+1)] = nums[-(i+1)], nums[i+k]

    # 3번풀이 O(N) -> 12ms, 메모리 약간 더
    def rotate(self, nums: [int], k: int) -> None:
        stack1 = []
        stack2 = []

        n = len(nums)

        k %= n
        count = 0

        for _ in range(n):
            a = nums.pop()
            if count < k:
                count += 1
                stack1.append(a)
            else:
                stack2.append(a)

        for _ in range(n):
            if len(stack1) > 0:
                a = stack1.pop()
            else:
                a = stack2.pop()
            nums.append(a)

    # # 1번 풀이  O(N*K)
    def rotate(self, nums: [int], k: int) -> None:
        k %= len(nums)

        for _ in range(k):
            a = nums.pop()
            nums.insert(0,a)

a = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
a.rotate(nums, k)

