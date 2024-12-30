

from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_dic = defaultdict(int)
        word2_dic = defaultdict(int)

        for i in range(len(word1)):
            word1_dic[word1[i]] += 1
            word2_dic[word2[i]] += 1

        for k, v in word1_dic.items():
            if k not in word2_dic:
                return False

        w1_list = list(word1_dic.values())
        w2_list = list(word2_dic.values())
        w2_list.sort()
        w1_list.sort()

        for i in range(len(w1_list)):
            if w1_list[i] != w2_list[i]:
                return False
        return True


a = Solution()
word1 = "abc"
word2 = "bca"
print(a.closeStrings(word1, word2))



