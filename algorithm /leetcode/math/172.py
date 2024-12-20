
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        # 핵심은 5의 개수!! 10을 만들어야함. 2는 5보다 훨씬 많으니 고려 안해도 된다
        #  5, 10, 15, 20 -> 5가 1개
        #  25 -> 5가 2개..   125 -> 5가 3개 ..  5**1, 5**2 ??
        #  50 -> 5*5*2   75 ->5*5*3
        # 5의 제곱수가 아닌 것을 어떻게 계산하는냐가 문제였음..

        while n > 0:
            n //= 5
            count += n
        return count



a = Solution()
n =50
print(a.trailingZeroes(n))