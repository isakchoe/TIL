


class Solution:

    def longestConsecutive(self, nums: [int]) -> int:

        answer = 0

        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1

        visited = [False] * len(nums)

        def minus_count(num, count):
            dic[num] = 0
            if num-1 in dic:
                count += 1
                return minus_count(num-1, count)
            else:
                return count


        def plus_count(num, count):
            dic[num] = 0
            if num + 1 in dic:
                count += 1
                return plus_count(num+1, count)
            else:
                return count


        for num in nums:
            # visited
            if dic[num] == 0:
                continue
            minus = minus_count(num, 1)
            plus = plus_count(num, 1)

            temp_answer = minus + plus -1
            answer = max(answer, temp_answer)

        return answer




a = Solution()
nums = [100,4,200,1,3,2]
print(a.longestConsecutive(nums))














