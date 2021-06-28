def solution(s):
    #     스택 이용

    if s[0] != "(":
        return False

    stack = []
    stack.append(s[0])

    for i in range(1, len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True
