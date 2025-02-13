
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        window_size = len(part)

        while True:
            start = 0
            end = window_size

            flag = 0
            while end <= len(s):
                temp = s[start: end]

                if temp == part:
                    s = s[0:start] + s[end:]
                    flag += 1
                    break
                else:
                    start += 1
                    end += 1
            if flag == 0:
                break
        return s