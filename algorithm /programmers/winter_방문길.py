

def solution(dirs):
    # parsing,
    #  now, next ==> 범위 안에 드는지 확인
    #  now - next ==> 구간을 딕으로 저장

    # parsing
    dirs = list(dirs)

    dic ={}

    x = y = 0

    count = 0


    for i in range(len(dirs)):
        if dirs[i] == "U":
            n_x = x
            n_y = y+1
        elif dirs[i] == "D":
            n_x = x
            n_y = y -1
        elif dirs[i] == "R":
            n_x = x + 1
            n_y = y
        else:
            n_x = x-1
            n_y = y


#         범위 확인
        if  -5<=n_x <=5 and  -5<=n_y <=5:
#             중복 확인
            if  n_x == x:
                if n_y > y:
                    if (n_x,n_y,x,y) not in dic:
                        dic[(n_x,n_y,x,y)] = True
                        count += 1

                else:
                    if (x,y,n_x,n_y) not in dic:
                        dic[(x,y,n_x,n_y)] = True
                        count += 1

            else:
                if n_x > x:
                    if (n_x,n_y,x,y) not in dic:
                        dic[(n_x,n_y,x,y)] = True
                        count += 1

                else:
                    if (x,y,n_x,n_y) not in dic:
                        dic[(x,y,n_x,n_y)] = True
                        count += 1

            x = n_x
            y = n_y

    return count



