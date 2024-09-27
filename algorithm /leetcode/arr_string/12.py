

class Solution:
    def intToRoman(self, num: int) -> str:

        roman_dic = {
          1 : "I",
          5 : "V",
          10: "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }

        answer = []
        count = 0

        while num > 0:
            mod = num % 10
            mod_value = mod * (10 ** count)
            num = num // 10

            if mod_value in roman_dic:
                answer.append(roman_dic[mod_value])

            # 6,7,8
            elif mod > 5:
                if count == 0:
                    temp = "V"
                    for i in range(mod - 5):
                        temp += "I"
                elif count == 1:
                    temp = "L"
                    for i in range(mod -5):
                        temp += "X"
                else:
                    temp = "D"
                    for i in range(mod -5):
                        temp += "C"
                answer.append(temp)

            # 0,2,3,
            elif mod < 5:
                temp = ""
                for i in range(mod):
                    if count == 0:
                        temp += "I"
                    elif count == 1:
                        temp += "X"
                    elif count == 2:
                        temp += "C"
                    else:
                        temp += "M"
                answer.append(temp)

            count += 1

        answer.reverse()
        return "".join(answer)


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dic = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        answer = []

        for value, symbol in roman_dic:
            # While the number is greater than the current value
            while num >= value:
                num -= value
                answer.append(symbol)

        return ''.join(answer)



a = Solution()

num = 3749

print(a.intToRoman(num))

