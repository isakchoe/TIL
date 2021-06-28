
def solution(s):
    #     스택
    #     선형 탐색 하면서 마지막에 비면 1, 안비면 0
    stack = []

    s = list(s)
    # print(s)

    stack.append(s[0])
    # print(stack)

    for i in range(1 ,len(s)):
        if len(stack) !=0 and stack[-1] == s[i]:
            stack.pop()
            continue
        else:
            stack.append(s[i])

    if len(stack) == 0:
        return 1
    else:
        return 0