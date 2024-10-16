
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:

        word_dic = {}

        for w in wordDict:
            word_dic[w] = True

        dp_dic = {}

        # dp_dic 만들기
        for i in range(1, len(s) + 1):
            temp = s[0:i]

            if temp in word_dic:
                dp_dic[temp] = True
            else:
                #  조합 확인...
                for j in range(len(temp)):
                    front = temp[0:j]
                    back = temp[j:]

                    # worddic 조합으로 가능하다.
                    if (front in dp_dic or front in word_dic) and (back in dp_dic or back in word_dic):
                        dp_dic[temp] = True


        for i in range(1, len(s ) +1):
            temp = s[0:i]
            other_temp = s[i:]


            # word_dic 에 원래 있거나, 조합 가능한 경우
            if temp in word_dic or (temp in dp_dic and dp_dic[temp]):
                if len(other_temp) > 0:
                    if other_temp in word_dic or (other_temp in dp_dic and dp_dic[other_temp]):
                        return True
                    else:
                        dp_dic[temp] = False
                else:
                    return True
            else:
                dp_dic[other_temp] = False
        return False

a = Solution()
s = "catsandogcat"
wordDict = ["cats","dog","sand","and","cat","an"]
print(a.wordBreak(s, wordDict))
