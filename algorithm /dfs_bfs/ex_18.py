
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