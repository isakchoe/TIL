

def find_p(x, parent):
    if x != parent[x]:
        parent[x] = find_p(parent[x], parent)
    return parent[x]

def union(a, b, parent):

    a_result = find_p(a, parent)
    b_result = find_p(b, parent)

    if a_result > b_result:
        parent[a_result] = b_result
    else:
        parent[b_result] = a_result



def solution(commands):
    answer = []

    matrix = [["EMPTY"] * 51 for _ in range(51)]

    parent = [x  for x in range(2501)]

    for com in commands:
        c_list = com.split(" ")

        crud = c_list[0]

        if crud == "UPDATE":
            if len(c_list) == 4:
                update(int(c_list[1]), int(c_list[2]), c_list[3], matrix, parent)
            else:
                update_value(c_list[1], c_list[2], matrix, parent)

        elif crud == "MERGE":
            merge(int(c_list[1]), int(c_list[2]), int(c_list[3]),int(c_list[4]), matrix, parent)
        elif crud == "UNMERGE":
            unmerge(int(c_list[1]), int(c_list[2]),matrix, parent)
        else:

            result = select(int(c_list[1]), int(c_list[2]), matrix, parent)
            answer.append(result)


    return answer

def select(r,c ,matrix, parent):
    num = (r-1)*50 + c
    p = find_p(num, parent)
    nr, nc = get_nr_nc(p)

    return matrix[nr][nc]


def update_value(value, value2, matrix, parent):
    visited = [False] * 2501

    for i in range(1, 2501):
        num = find_p(i, parent)

        if visited[num]:
            continue

        nr, nc = get_nr_nc(num)

        if matrix[nr][nc] == value:
            matrix[nr][nc] = value2

        visited[num] = True

def get_nr_nc(node_num):
    if node_num % 50 == 0:
        nr = node_num // 50
        nc = 50
        return [nr, nc]

    nr =  node_num // 50 +1
    nc =  node_num - 50*(nr-1)
    return [nr, nc]



def update(r, c, new_value, matrix, parent):
    num = (r-1) * 50 + c
    root = find_p(num, parent)

    nr, nc = get_nr_nc(root)

    # update - 부모를 업데이트
    matrix[nr][nc] = new_value



def merge(r, c, r2, c2, matrix, parent):

    n1 = (r-1) *50 + c
    n2 = (r2-1)*50 + c2

    p_1 = find_p(n1, parent)
    p_2 = find_p(n2, parent)

    nr1, nc1 =  get_nr_nc(p_1)
    nr2, nc2 = get_nr_nc(p_2)

    p_value = matrix[nr1][nc1]
    p_value2 = matrix[nr2][nc2]

    if p_value == "EMPTY" and p_value2 != "EMPTY":
        matrix[nr1][nc1] = p_value2
        parent[p_1] = p_2
    else:
        matrix[nr2][nc2] = p_value
        parent[p_2] = p_1



def unmerge(r,c, matrix, parent):

    # update
    for i in range(1,2501):
        find_p(i, parent)


    num = (r-1) *50 + c

    p = parent[num]

    nr, nc = get_nr_nc(p)
    origin = matrix[nr][nc]

    for i in range(1, 2501):
        if parent[i] == p:
            # 자기 자신으로 초기화
            parent[i] = i
            nr, nc = get_nr_nc(i)

            if nr == r and nc == c:
                matrix[nr][nc] = origin
            else:
                matrix[nr][nc] = "EMPTY"




commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group",
            "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

print(solution(commands))