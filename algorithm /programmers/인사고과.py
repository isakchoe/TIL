
def solution(scores):
    my_ati = scores[0][0]
    my_co = scores[0][1]

    scores.sort(key = lambda x: (-x[0], x[1]))

    arr_filter = [sum(scores[0])]

    last_start = scores[0][0]
    last_end = scores[0][1]


    for i in range(1, len(scores)):
        if last_start == scores[i][0]:
            last_end = scores[i][1]
            arr_filter.append(scores[i][0] + scores[i][1])
        else:
            # 정상... 앞 작아지고, 뒤 같거나 커지는
            if scores[i][1] >= last_end:
                last_start = scores[i][0]
                last_end = scores[i][1]
                arr_filter.append(scores[i][0] + scores[i][1])
            else:
                # 베제헤야함
                if scores[i][0] == my_ati and scores[i][1] == my_co:
                    return -1


    arr_filter.sort(reverse=True)

    for idx, num in enumerate(arr_filter):
        if num == my_ati + my_co:
            return idx +1




