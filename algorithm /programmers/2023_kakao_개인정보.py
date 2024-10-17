

def solution(today, terms, privacies):

    today_to_day = convert_to_day(today)

    dic = {}

    for t in terms:
        temp_list = t.split(" ")
        name = temp_list[0]
        month = int(temp_list[1])

        dic[name] = month*28

    answer = []

    for idx, p in enumerate(privacies):
        t_list = p.split(" ")
        origin = t_list[0]
        name = t_list[1]

        origin_day = convert_to_day(origin)

        expired_day = origin_day + dic[name]

        if expired_day <= today_to_day:
            answer.append(idx+1)

    return answer


def convert_to_day(time_format):
    t_list = time_format.split(".")

    y = int(t_list[0])
    m = int(t_list[1])
    d = int(t_list[2])
    return (y-2000) * 12*28 + m*28 + d



today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))