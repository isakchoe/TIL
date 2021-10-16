def main():

    n, m = map(int, input().split())

    data = list(map(int, input().split()))

    matrix = []

    check_matrix = [ [0]*m for _  in range(n) ]



    for  i in range(n):
        li = list(map(int, input().split()))
        matrix.append(li)



    x = data[0]
    y = data[1]
    look = data[2]

    check_matrix[x][y] = 1

    look_sequence = [-1,0,1,2]

    move = [(0,-1), (-1,0), (0,1), (1,0)]

    answer = 1

    turn_time = 0

    while True:

        for i in range(len(look_sequence)):
            if look -1 == look_sequence[i]:
                new_x = x + move[i][0]
                new_y = y + move[i][1]
                look = look -1
                if look == -1:
                    look = 3

                if matrix[new_x][new_y] != 1 and check_matrix[new_x][new_y] != 1:
                    x = new_x
                    y = new_y

                    answer += 1
                    check_matrix[new_x][new_y] = 1
                    break


                else:
                    turn_time += 1
                    if turn_time == 4:
                        x = x - move[i][0]
                        y = y - move[i][1]

                        if matrix[x][y] != 1:
                            turn_time = 0
                            continue

                        else:
                            break

        if turn_time == 4:
            break


    print(answer)


main()






