def main():

    n = int(input())
    num_apple = int(input())

    apple_loca = []

    for i in range(num_apple):
        x,y = map(int,input().split())
        apple_loca.append([x-1,y-1])

    num_turn = int(input())

    turn_list=[]

    for i in range(num_turn):
        time, look = input().split()
        turn_list.append([int(time),look])


    head_row = 0
    head_col = 0

    path_list = [[head_row,head_col]]

    dir = 'R'

    map = [[0]*n for _ in range(n)]


    # 사과 놓인 곳을 1로 만듬.
    for i in range(num_apple):
        x, y = apple_loca[i][0], apple_loca[i][1]
        map[x][y] = 1

    time = 0

    while True:

        head_row , head_col = path_list[-1][0], path_list[-1][1]

        for i in range(len(turn_list)):
            if time == turn_list[i][0]:
                dir = turn_list[i][1]




        if dir == "R":
            if map[path_list[-1][0]][path_list[-1][1]+1] != 1:
                path_list.pop(0)

            path_list.append([path_list[-1][0], path_list[-1][1] + 1])

        if dir == "L":
            if map[head_row][head_col-1] != 1:
                path_list.pop(0)

            path_list.append([head_row, head_col-1])

        if dir == "U":
            if map[head_row-1][head_col] !=1:
                path_list.pop(0)

            path_list.append([head_row-1, head_col])

        if dir == "D":
            if map[head_row+1, head_col] !=1:
                path_list.pop(0)
            path_list.append([head_row+1, head_col])


        time +=1


        if  path_list[-1][0] > n or path_list[-1][0] < 0 or path_list[-1][1] > n or path_list[-1][1] < 0 :
            break

        # 몸이 부딪히는 경우
        for i in range(len(path_list)-1):
            for j in range(i+1, len(path_list)):
                if path_list[i] == path_list[j] :
                    break



    print(time)
    