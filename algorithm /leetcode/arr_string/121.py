

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        answer = 0
        buy_price = prices[0]
        sell_price = prices[0]

        # 낮아지는 지점 찾고... 올라가는 꼭대기 찾기..
        for i in range(1, len(prices)):
            p = prices[i]
            # 최고점..
            if p > sell_price:
                sell_price = p
                answer = max(answer, sell_price - buy_price)
            if p < buy_price:
                # 같이 초기화 해야함...
                buy_price = p
                sell_price = p
        return answer

a = Solution()
prices = [3,2,6,5,0,3]
print(a.maxProfit(prices))

