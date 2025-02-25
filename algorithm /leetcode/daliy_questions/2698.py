from itertools import combinations


class Solution:
    def punishmentNumber(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if self.check(i):
                total += i * i
        return total

    def check(self, num):
        square = num * num

        if num == square:
            return True

        str_p = str(square)
        n = len(str_p)

        result = []

        # 이게 핵심!!... 외우자.. helped from gpt
        # 2자리 이상인 수...
        for cut in range(1, n):  # 몇번 자를것인가
            for combi in combinations(range(1, n), cut):
                pre = 0

                split = []
                for i in combi:
                    temp = str_p[pre:i]
                    split.append(temp)
                    pre = i

                    # 마지막 처리
                split.append(str_p[pre:])

                result.append(split)

        for r in result:
            temp_list = map(int, r)
            temp_sum = sum(temp_list)

            if temp_sum == num:
                return True

        return False

