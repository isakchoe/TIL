
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(s_list) != len(pattern):
            return False

        dic = {}
        word_set = set()

        for idx, string in enumerate(s_list):
            key = pattern[idx]

            if key not in dic:
                if string in word_set:
                    return False
                dic[key] = string
                word_set.add(string)
            else:
                if dic[key] != string:
                    return False
        return True


a = Solution()
pattern = "abba"
s = "dog dog dog dog"
print(a.wordPattern(pattern, s))
