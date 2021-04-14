

def solution(answers):
    answer = []

    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in range(len(answers)):
        # 1번
        if answers[i] == (i) % 5 + 1:
            count_1 += 1
        #         2번
        if answers[i] == 2 and i % 2 == 0:
            count_2 += 1

        if i % 8 == 1 and answers[i] == 1 or i % 8 == 3 and answers[i] == 3 or i % 8 == 5 and answers[
            i] == 4 or i % 8 == 7 and answers[i] == 5:
            count_2 += 1
        #         3번

        if (i % 10 == 0 or i % 10 == 1) and answers[i] == 3:
            count_3 += 1

        if (i % 10 == 2 or i % 10 == 3) and answers[i] == 1:
            count_3 += 1

        if (i % 10 == 4 or i % 10 == 5) and answers[i] == 2:
            count_3 += 1
        if (i % 10 == 6 or i % 10 == 7) and answers[i] == 4:
            count_3 += 1
        if (i % 10 == 8 or i % 10 == 9) and answers[i] == 5:
            count_3 += 1

    result = max(count_1, count_2, count_3)
    temp = [count_1, count_2, count_3]


    for i in range(3):
        if temp[i] == result:
            answer.append(i+1)

    return answer