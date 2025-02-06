

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        count = 0

        to_change = []
        for i in range(n):
            if s1[i] != s2[i]:
                to_change.append(i)
                count += 1

        if len(to_change) != 2:
            return False

        front = to_change[0]
        end = to_change[1]

        if s2[front] == s1[end] and s2[end] == s1[front]:
            return True
        return False




a = Solution()
s1 = "abcd"
s2 = "dcba"
print(a.areAlmostEqual(s1,s2))

