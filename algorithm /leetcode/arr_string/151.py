

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)




a = Solution()
s =  "  hello world  "
print(a.reverseWords(s))
