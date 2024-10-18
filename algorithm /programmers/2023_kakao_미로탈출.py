


def solution(n, m, x, y, r, c, k):
    answer = ""

    nx = x
    ny = y
    nr = r
    nc = c
    nk = k


    while more_go(nx, ny, nr, nc, nk):
        nx, ny, route = go_desc_sort(n,m,nx,ny)

        answer += route
        nk -= 1

    temp = go_short(nx, ny, nr, nc)
    answer += temp

    if len(answer) != k:
        return "impossible"
    return answer


def more_go(x, y, r, c, k):
    left = abs(x-r) + abs(y-c)

    if left < k:
        return True

    return False

def go_short(x,y,r,c):
    answer = ""
    # d
    if x < r:
        answer += (r-x)*"d"

    # l
    if y > c:
        answer += (y-c)*"l"

    # r
    if y < c:
        answer += (c-y)*"r"

    # u
    if x > r:
        answer += (x-r)*"u"

    return answer



def go_desc_sort(n,m,x,y):

    route = ""
    # d
    if  x < n:
        x += 1
        route += "d"

    # l
    elif x == n:
        if y > 1:
            y -= 1
            route += "l"
        else:
            # r
            if y < m:
                y += 1
                route += "r"
            else:
                # u
                if x > 1:
                    x -= 1
                    route += "u"

    return [x,y, route]


#
# def get_short_route(x,y,r,c):
#
#     short_route = []
#
#     # l or r ?
#     if c > y:
#         temp = c - y
#         for _ in range(temp):
#             short_route.append("r")
#     else:
#         temp = y - c
#         for _ in range(temp):
#             short_route.append("l")
#
#     if r > x:
#         temp = r - x
#         for _ in range(temp):
#             short_route.append("d")
#     else:
#         temp = x - r
#         for _ in range(temp):
#             short_route.append("u")
#
#     short_route.sort()
#
#     return ''.join(short_route)
#



n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5

print(solution(n, m, x, y, r, c, k))




