def knight():
    n = input()



    row_list = {'a':1 , 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,'g':7,'h':8}

    x = row_list[n[0]]
    y = int(n[1])

    answer = 0

    move_list = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

    for i in move_list:
        new_x = x + i[0]
        new_y = y + i[1]

        if new_x >=1 and new_x <=8 and new_y >=1 and new_y <=8:
            answer += 1


    print(answer)




knight()
