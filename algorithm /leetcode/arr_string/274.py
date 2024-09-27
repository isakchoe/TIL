

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        answer = 0
        for idx, ci_count in enumerate(citations):
            if ci_count >= idx+1:
                answer += 1
        return answer


a = Solution()
citations = [1,3,1]
print(a.hIndex(citations))