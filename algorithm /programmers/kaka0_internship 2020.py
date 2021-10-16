
# 거리 구하는 함수
def dis(n1, n2):
    # 숫자패드 위치 좌표로 전환
    num = [(1, 0), (0, 3), (1, 3), (2, 3), (0, 2), (1, 2), (2, 2), (0, 1), (1, 1), (2, 1), [0, 0], [2, 0]]

    if n2 == "#":
        b = num[11]
    elif n2 == "*":
        b = num[10]
    else:
        b = num[n2]
    a = num[n1]

    result = abs(a[0] - b[0]) + abs(a[1] - b[1])

    return result


def solution(numbers, hand):
    answer = ''

    # 시작 위치,  "*" 은 10번 , "#" 은 11번
    r_index = 11
    l_index = 10

    # 숫자들 선형 탐색
    for num in numbers:
        # 왼손범위
        if num in [1, 4, 7]:
            answer += 'L'
            l_index = num

        # 오른손 범위
        elif num in [3, 6, 9]:
            answer += 'R'
            r_index = num
        # 중간범위
        else:
            # 왼손, 오른손으로부터 눌러야할 키패드 위치 계산
            l_distance = dis(num, l_index)
            r_distance = dis(num, r_index)

            # 오른손이 작은 경우
            if l_distance > r_distance:
                answer += "R"
                r_index = num
            # 왼손이 작은 경우
            elif l_distance < r_distance:
                answer += "L"
                l_index = num

            # 거리 같은 경우
            else:
                # 오른손 잡이
                if hand == "right":
                    answer += "R"
                    r_index = num
                # 왼손잡이
                else:
                    answer += "L"
                    l_index = num

    return answer