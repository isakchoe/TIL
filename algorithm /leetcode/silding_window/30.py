import copy

# O(N)
class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        dic = {}
        word_dic = {}

        for w in words:
            start = w[0]

            if w not in word_dic:
                word_dic[w] = 1
            else:
                word_dic[w] += 1

            if start not in dic:
                dic[start] = True

        n = len(s)

        total_len = len(words) * len(words[0])
        step = len(words[0])

        answer = []

        for i in range(n):
            # substring 의미 없.
            if n - i < total_len:
                break

            if s[i] not in dic:
                continue

            if self.is_sub(s[i:i+total_len], copy.deepcopy(word_dic), step):
                answer.append(i)

        return answer

    def is_sub(self, s_arr, word_dic, step):

        for i in range(0, len(s_arr), step):
            temp = s_arr[i:i+step]

            if temp not in word_dic or word_dic[temp] == 0:
                return False

            word_dic[temp] -= 1

        for k,v in word_dic.items():
            if v !=0:
                return False
        return True



a = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(a.findSubstring(s,words))


