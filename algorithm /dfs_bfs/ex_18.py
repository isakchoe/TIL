
def dfs(para):
    right = 0
    left = 0

    if para == '':
        return para


    for i in range(len(para)):
        if para[i] == "(":
            left += 1
        if para[i] == ")":
            right += 1

        # 개수 같으면, 균형잡힌 문자 최소 길이로 만들기
        if right == left:
            u = para[0:i+1]
            v = para[i+1:]
            break

    check = 0
    start = u[0]
    for i in range(len(u)):
        if u[i] != start:
            check += 1
            start = u[i]

    # 올바른 괄호 문자인지 확인,, 변하는 횟수가 홀수여야 한다.
    if u[0] == "(" and check%2 == 1:
        temp = dfs(v)
        return u + temp
    else:
        temp = "(" + dfs(v) + ")"

        u = u[1:-1]

        result = ''

        for i in range(len(u)):
            if u[i] == "(":
                result += ")"

            else:
                result += "("

        return temp +result




def solution(p):

    return dfs(p)