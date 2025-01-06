

class Solution:
    def minOperations(self, boxes: str) -> [int]:
        n = len(boxes)
        answer = [0] * n

        indexs = []

        for i in range(n):
            if boxes[i] == "1":
                indexs.append(i)

        for i in range(n):
            total = 0
            for idx in indexs:
                total += abs(i - idx)
            answer[i] = total
        return answer

a = Solution()
boxes ="001011"
print(a.minOperations(boxes))

