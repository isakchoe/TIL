
def possible(result):

    for temp in result:
        x,y,stuff = temp

        if stuff == 0:

            if y == 0 or [x,y-1,0] in result or [x-1,y,1] in result or [x,y,1] in result:
                continue
            else:
                return False

        if stuff == 1:

            if [x-1,y,1] in result and [x+1,y,1]in result or [x,y-1,0] in result or [x+1,y-1,0] in result:
                continue
            else:
                return False

    return True





def solution(n, build_frame):
    result = []

    for build in build_frame:
        x,y,stuff, operate = build

        # 삭제
        if operate == 0:
            result.remove([x,y,stuff])
            if  not possible(result):
                result.append([x,y,stuff])

        # 설치
        if operate == 1:
            result.append([x,y,stuff])
            if not possible(result):
                result.remove([x,y,stuff])

    return sorted(result)







