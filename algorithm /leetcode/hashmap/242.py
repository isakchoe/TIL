

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic = {}

        for string in s:
            if string not in dic:
                dic[string] = 1
            else:
                dic[string] += 1


        for string in t:
            if string not in dic:
                return False
            else:
                if dic[string] == 0:
                    return False
                dic[string] -= 1

        for k,v in dic.items():
            if v !=0:
                return False
        return True