

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_idx = 0
        t_idx = 0

        count = 0

        while s_idx < len(s) and t_idx < len(t):
            s_value = s[s_idx]
            t_value = t[t_idx]

            if s_value == t_value:
                s_idx += 1
                t_idx += 1
                count += 1
            else:
                t_idx += 1

        if count == len(s):
            return True
        return False




