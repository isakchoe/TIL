
# 두번째 풀이



def rotate(arr):
    length = len(arr)

    result = [[0] * length for _ in range(length)]

    # 회전 구현도 까다롭다
    for i in range(length):
        for e in range(length):
            result[e][length - i - 1] = arr[i][e]

    return result


def check(lock):
    length = len(lock) // 3

    for i in range(length, 2 * length):
        for e in range(length, 2 * length):
            if lock[i][e] != 1:
                return False

    return True


def solution(key, lock):
    length = len(lock)
    new_lock = [[0] * 3 * length for _ in range(3 * length)]

    # new_lock 3배 만들기  -- 문제의 핵심!아이디어
    for i in range(len(lock)):
        for e in range(len(lock)):
            new_lock[i + length][e + length] = lock[i][e]

    # 회전 총 4번
    for i in range(4):
        # 새로운 변수 만들면 안된다. 한번만 회전하니깐,,,  
        key = rotate(key)

        # 자물쇠랑 열쇠 결합 => 각 요소별 합치는 것! ==> 전부 1인지 체크 ==> true or false.  구현이 까다롭다
        for r in range(2 * length):
            for c in range(2 * length):
                for k_r in range(len(new_key)):
                    for k_c in range(len(new_key)):
                        # 핵심 구현요소! lock시작점 + key 행 열 합하면 된다
                        new_lock[r + k_r][c + k_c] += new_key[k_r][k_c]

                if check(new_lock):
                    return True
                else:
                    for x in range(len(new_key)):
                        for y in range(len(new_key)):
                            new_lock[r + x][c + y] -= new_key[x][y]

    return False