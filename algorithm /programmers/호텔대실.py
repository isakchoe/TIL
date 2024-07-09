



def parse_time(time_str):
    arr = time_str.split(":")
    return (int(arr[0])*60) + int(arr[1])




def solution(book_time):
    time_arr = [0] * (60*24)

    for start, end in book_time:
        start_time = parse_time(start)
        end_time = parse_time(end)

        time_arr[start_time] += 1

        if end_time + 10 < 60*24:
            time_arr[end_time + 10] -= 1

    for i in range(1, len(time_arr)):
        time_arr[i] += time_arr[i-1]

    return max(time_arr)


def solution(book_time):
    room_count = 0
    reservation_dict = {}

    for time in book_time:
        start_time, end_time = map(int, time)

        # 예약 시작 시각에 해당 객실을 사용 중으로 표시
        if start_time in reservation_dict:
            reservation_dict[start_time] += 1
        else:
            reservation_dict[start_time] = 1

        # 예약 종료 시각에 해당 객실을 사용 종료로 표시
        if end_time in reservation_dict:
            reservation_dict[end_time] -= 1
        else:
            reservation_dict[end_time] = -1

    # 시각을 기준으로 정렬
    sorted_times = sorted(reservation_dict.keys())

    # 현재 사용 중인 객실 수를 세면서 최소 객실 수 갱신
    current_rooms = 0
    for time in sorted_times:
        current_rooms += reservation_dict[time]
        room_count = max(room_count, current_rooms)

    return room_count