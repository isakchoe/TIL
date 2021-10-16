
from bisect import bisect_left, bisect_right



def solution(words, queries):

    answer = []

    # 일반리스트, 역순리스트 생성
    arr = [ [] for _ in range(10001)]
    r_arr = [ [] for _ in range(10001)]

    # 단어 길이!에 따라서 필터링!! 중요!!
    for i in range(len(words)):
        arr[len(words[i])].append(words[i])
        r_arr[len(words[i])].append(words[i][::-1])

    #     정렬
    for i in range(10001):
        arr[i].sort()
        r_arr[i].sort()

    for i in range(len(queries)):
        # ?가 제일 앞이면, 뒤집어야지 제대로 정렬 순서 비교가 가능하다.
        if queries[i][0] == '?':
            # 바이섹트 라이브러리 활용
            front = queries[i][::-1].replace('?', 'a')
            back = queries[i][::-1].replace('?', 'z')

            left_index = bisect_left(r_arr[len(queries[i])], front )
            right_index = bisect_right(r_arr[len(queries[i])], back)

            result = right_index - left_index

        #         접미사인 경우
        else:
            front = queries[i].replace("?" ,"a")
            back = queries[i].replace("?", 'z')

            left_index = bisect_left(arr[len(queries[i])], front)
            right_index = bisect_right(arr[len(queries[i])], back)

            result = right_index - left_index

        answer.append(result)

    return answer


