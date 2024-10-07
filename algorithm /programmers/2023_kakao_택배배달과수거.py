def solution(cap, n, deliveries, pickups):
    p_stack = []
    d_stack = []

    for i in range(n):
        if deliveries[i] != 0:
            d_stack.append([i, deliveries[i]])
        if pickups[i] != 0:
            p_stack.append([i, pickups[i]])

    answer = 0

    while len(p_stack) > 0 or len(d_stack) > 0 :
        cost = one_go_and_return(cap, d_stack, p_stack)
        answer += cost

    return answer

def one_go_and_return(cap, deliveries, pickups):
    # 가장 먼 pick_up, 배달지를 최우선으로 간다..
    #  가장 먼 곳이 배달지라면, 차고에서 갖고 간다...
    #  자리가 남고 && 배달할 곳이 더 있다면 더 채운다.

    #  배달 갖다 돌아오면서 수거한다...

    next_pickup = 0

    #  항상 예외 처리 중요! - 픽업, 배달 둘 중 하나는 먼저 끝날 수도 있다.
    if len(pickups) > 0:
        next_pickup = pickups[-1][0]

    next_deliver = 0
    if len(deliveries) > 0:
        next_deliver = deliveries[-1][0]

    # 다음에 갈 가장 먼 곳 선정
    next_home = max(next_pickup, next_deliver)

    cost = (next_home+1) * 2


    # deliver 세팅
    for i in range(cap):
        if len(deliveries) == 0:
            break
        if deliveries[-1][1] != 0:
            deliveries[-1][1] -= 1
            if deliveries[-1][1] == 0:
                # 스택을 이용해서.. 시간복잡도를 줄인다!!
                deliveries.pop()

    # pick up
    for i in range(cap):
        if len(pickups) == 0:
            break
        if pickups[-1][1] != 0:
            pickups[-1][1] -= 1
            if pickups[-1][1] == 0:
                pickups.pop()

    return cost

cap = 2
n = 7
d = [1, 0, 2, 0, 1, 0, 2]
p = [0, 2, 0, 1, 0, 2, 2]


print(solution(cap, n, d, p))