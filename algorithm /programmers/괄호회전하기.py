from collections import deque


def is_correct(s):
    stack = []

    for string in s:
        if string in ['(', '[', '{']:
            stack.append(string)
        else:
            if string == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif string == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            elif string == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

    if len(stack) != 0:
        return False
    return True


def solution(s):
    q = deque()

    for string in s:
        q.append(string)

    count = 0

    for i in range(len(s)):
        front = q.popleft()
        q.append(front)

        result = is_correct(q)

        if result:
            count += 1

    return count