
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        idx = 0

        while idx < len(s):
            roman = s[idx]

            if roman == "I":
                if idx < len(s) -1:
                    if s[idx + 1] == "V":
                        total += 4
                        idx +=2
                        continue
                    elif s[idx + 1] == "X":
                        total += 9
                        idx += 2
                        continue
                total += 1
                idx += 1

            elif roman == "X":
                if idx < len(s) - 1:
                    if s[idx + 1] == "L":
                        total += 40
                        idx += 2
                        continue
                    elif s[idx + 1] == "C":
                        total += 90
                        idx += 2
                        continue
                total += 10
                idx += 1

            elif roman == "C":
                if idx < len(s) - 1:
                    if s[idx + 1] == "D":
                        total += 400
                        idx += 2
                        continue
                    elif s[idx + 1] == "M":
                        total += 900
                        idx += 2
                        continue
                total += 100
                idx += 1

            else:
                total += roman_dic[roman]
                idx += 1

        return total

a = Solution()
s = "MCMXCIV"
print(a.romanToInt(s))