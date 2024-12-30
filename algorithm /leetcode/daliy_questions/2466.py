


class Solution:
    # helped from gpt
    # 계단 오르기랑 거의 똑같. 근데 왜 유추를 못한 것인가.
    # append -> 맨뒤에 붙이는 것인가, 앞에 붙이는 것인가, 가운데 붙이는 것인가에 대한 혼란... -> 중복을 어캐 제거할까 고민햇음..
    # 순서가 바뀌면, dp 의 의미가 맞지 않음... -> dp(5) 는 5 글자수가 세팅되어있는거임..
    # dp(7) += dp(5), dp(7) +=dp(2) ,  one =2, zero = 5 일경우.. 순서는 결국 맞춰진다!!!
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        dp = [0] * (high+1)
        dp[0] = 1

        for i in range(1, high+1):
            if i >= one:
                dp[i] += dp[i-one]

            if i >= zero:
                dp[i] += dp[i-zero]

            dp[i] % (10**9 +7)

        answer = sum(dp[low:high+1])
        return answer % (10**9 + 7)




a = Solution()
low = 3
high = 3
zero = 1
one = 1
print(a.countGoodStrings(low,high,zero,one))