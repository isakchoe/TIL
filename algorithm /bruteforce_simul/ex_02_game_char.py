def main():

    n, m = int(input().split())

    data = list(map(int, input().split()))

    matrix = []

    for  i in range(n):
        li = list(map(int, input().split()))
        matrix.append(li)



    x = data[0]
    y = data[1]
    look = data[2]

    look_sequence = [-1,0,1,2]

    move = [(-1,0), (0,-1), (1,0), (0,1)]

    answer = 0

    for i in range(len(look_sequence)):
        if look -1 == look_sequence[i]:
            new_x = x + move[i][0]
            new_y = y + move[i][1]

            if matrix[new_x][new_y] != 1:
                x = new_x
                y = new_y
                look = look -1
                answer += 1



