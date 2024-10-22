
def convert_clear(s_list):
    temp = ""
    formated_list = ["("]
    for s in s_list:
        # 괄호 제거, 숫자, 연산자만
        if s == " " or s == '':
            continue

        if s == "(" :
            formated_list.append(s)
            continue

        elif s == ")":
            if temp != "":
                formated_list.append(temp)
            formated_list.append(s)
            temp = ""
            continue

        if s == "+" or s == "-":
            if temp != "":
                formated_list.append(temp)
            formated_list.append(s)
            temp = ""
        else:
            temp += s

    if temp != "":
        formated_list.append(temp)

    formated_list.append(")")

    return formated_list



class Solution:
    def calculate(self, s: str) -> int:
        s_list = list(s)

        formated_list = convert_clear(s_list)

        if len(formated_list) == 3:
            return int(formated_list[1])


        num_stack = []

        for string in formated_list:
            if string == ")":
                temp = 0
                while True:
                    pop_stack = num_stack.pop()

                    if pop_stack == "(":
                        num_stack.append(temp)
                        break

                    pop_stack2 = num_stack.pop()

                    if pop_stack2 == "(":
                        temp += pop_stack
                        num_stack.append(temp)
                        break

                    elif pop_stack2 == "-":
                        temp -= pop_stack

                    elif pop_stack2 == "+":
                        temp += pop_stack


            elif string != "+" and string != "-" and string != "(" :
                num_stack.append(int(string))
            else:
                num_stack.append(string)

        return num_stack[-1]



a = Solution()

s = "- (3 + (4 + 5))"
print(a.calculate(s))