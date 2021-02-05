
def rotate_key(key):
    n = len(key)
    m = len(key[0])

    # n * m 행렬을 --> m * n 행열로 변환!

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for e in range(m):
            result[e][n-i-1] = key[i][e]

    return result




def check(new_lock):

    lock_length = len(new_lock)//3

    for i in range(lock_length, 2*lock_length):
        for e in range(lock_length, 2*lock_length):
            if new_lock[i][e] !=1:
                return False

    return True



def main(key,lock):

    length_lock = len(lock)

    length_key = len(key)


    # 3배 증가 시키기
    new_lock = [[0]* 3*length_lock for _ in range(3*length_lock) ]

    for i in range(length_lock):
        for j in range(length_lock):
            new_lock[i+length_lock][j+length_lock] = lock[i][j]


    for rotate in range(4):

        key = rotate_key(key)

        # 모든 범위를 확인할 필요없다.. 범위가 2 * length
        for row in range(2*length_lock):
            for col in range(2*length_lock):
                for key_row in range(length_key):
                    for key_col in range(length_key):

                        new_lock[row +key_row][col+key_col] += key[key_row][key_col]

                # 더해서 맞으면 리턴하고 틀리면 다시 열쇠를 빼야 한다.!
                if check(new_lock):
                    return True

                else:
                    for key_row in range(length_key):
                        for key_col in range(length_key):
                            new_lock[row + key_row][col+key_col] -= key[key_row][key_col]


    return False






    