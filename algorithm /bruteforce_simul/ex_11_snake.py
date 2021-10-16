

def main():

    n = int(input())
    num_apple = int(input())

    apple_loca = []

    for i in range(num_apple):
        x, y = map(int, input().split())
        apple_loca.append([x,y])

    num_turn = int(input())

    turn_list=[]

    for i in range(num_turn):
        time, look = input().split()
        turn_list.append([int(time),look])


    head_row = 1
    head_col = 1

    # 뱀의 몸통이 있는 좌표 삽입
    path_list = [(head_row,head_col)]


    dir = 'R'

    data = [[0]*(n+2) for _ in range(n+2)]


    # 사과 놓인 곳을 1로 만듬.
    for i in range(num_apple):
        x, y = apple_loca[i][0], apple_loca[i][1]
        data[x][y] = 1

    # 뱀이 있는 곳은 2로 만듬 
    data[head_row][head_col] = 2


    time = 0

    move = [[0,1], [1,0], [0,-1], [-1,0]]


    direction = 0

    while True:

        head_row , head_col = path_list[-1][0], path_list[-1][1]

        pro_row, pro_col = head_row +move[direction][0], head_col+move[direction][1]


        # 끝나지 않는경우
        if pro_row >0 and pro_row  <=n and pro_col >0 and pro_col <=n and data[pro_row][pro_col] !=2:

            if data[pro_row][pro_col] !=1:
                rx,ry = path_list.pop(0)
                data[rx][ry] = 0

            path_list.append([pro_row, pro_col])
            data[pro_row][pro_col] = 2

            time +=1

        # 끝나는 경우
        else:
            time +=1
            break


        # 회전하는 시간!
        for i in range(len(turn_list)):
            if time == turn_list[i][0]:
                dir = turn_list[i][1]
                if dir == "L":
                    direction = (direction - 1) % 4
                else:
                    direction = (direction + 1) % 4


    print(time)

main()
