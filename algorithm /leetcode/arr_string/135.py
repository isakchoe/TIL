
class Solution:
    def candy(self, ratings: [int]) -> int:
        answer = [1] * len(ratings)

        # 왼쪽보다 크면, +1
        # left -> right
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                answer[i]  = answer[i-1] + 1
        # 오른쪽보다 크면,
        # 역순으로 탐색
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                answer[i] = max(answer[i], answer[i+1] + 1)    # 핵심 로직..
        return sum(answer)

a = Solution()
ratings = [1,2,87,87,87,2,1]
print(a.candy(ratings))
