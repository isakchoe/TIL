

class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        dp = [10001] * (amount+1)

        #  화폐로 1번에
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        # O(amount * coins)
        for i in range(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[amount] == 10001:
            return -1
        return dp[amount]


a = Solution()
coins = [1, 2147483647]
amount = 2
print(a.coinChange(coins, amount))