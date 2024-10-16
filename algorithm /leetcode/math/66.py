

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        origin_num = ""
        for num in digits:
            origin_num += str(num)

        to_num = int(origin_num)
        to_num += 1

        answer = []

        while to_num > 0:
            temp = to_num % 10
            answer.append(temp)
            to_num = to_num // 10

        answer.reverse()

        return answer


a = Solution()
digits = [1,2,3]
print(a.plusOne(digits))