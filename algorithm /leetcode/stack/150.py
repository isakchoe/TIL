
import math

class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack = []
        operands = {"+": True, "-": True, "*":True, "/": True}

        for token in tokens:
            if token in operands:
                sec = stack.pop()
                first = stack.pop()

                if token == "+":
                    stack.append(first + sec)
                elif token == "-":
                    stack.append(first - sec)
                elif token == "*":
                    stack.append(first * sec)
                else:
                    result = first / sec

                    stack.append(math.trunc(result))
            else:
                stack.append(int(token))

        return stack[-1]

a = Solution()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(a.evalRPN(tokens))