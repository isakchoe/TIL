
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        answer = []

        if len(s) < 10:
            return answer

        start = 0
        end = 9

        dic = {}

        while end < len(s):
            temp = s[start: end+1]

            if temp not in dic:
                dic[temp] = 1
            else:
                dic[temp] += 1

            start += 1
            end += 1

        for k, v in dic.items():
            if v > 1:
                answer.append(k)
        return answer

a = Solution()
s = "AAAAAAAAAAAAA"
print(a.findRepeatedDnaSequences(s))




