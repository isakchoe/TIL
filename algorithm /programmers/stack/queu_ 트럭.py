from _collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque()

    #  큐 == 다리, 0으로 채워넣기
    for _ in range(bridge_length):
        q.append(0)

    index = 0
    time = 0
    total = 0

    #  초당 pop, push ==> 0 or 다음트럭
    while True:
        # 시간 경과, 맨앞 pop
        time += 1
        total -= q.popleft()

        # 다리 무게가 견딜 수 있으면, 트럭 진입 push
        if total + truck_weights[index] <= weight:
            q.append(truck_weights[index])
            total += truck_weights[index]

            index += 1

        # 진입못하면 0 push
        else:
            q.append(0)

        # 마지막 트럭 진입하면 break
        if index == len(truck_weights):
            break

    return time + bridge_length


