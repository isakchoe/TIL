
class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.dp = [1]
        self.max_idx = -1


    def add(self, num: int) -> None:
        self.arr.append(num)

        if num == 0:
            self.max_idx = len(self.arr) -1
            self.dp.append(1)
        else:
            self.dp.append(self.dp[-1] * num)

    # 핵심은.. 0 을 처리하는 것!
    def getProduct(self, k: int) -> int:

        k_idx = len(self.arr) - k

        if self.max_idx >= k_idx:
            return 0

        total = self.dp[-1]
        n = len(self.arr) - k
        part = self.dp[n]

        return (total // part)
