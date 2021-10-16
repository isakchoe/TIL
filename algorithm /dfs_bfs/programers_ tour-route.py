from collections import deque


def solution(tickets):
    answer = []
    q = deque()

    tickets.sort(key=lambda x: x[1])

    for i in tickets:
        if i[0] == "ICN":
            q.append([i[0], i[1]])
            break

    while q:
        fr, to = q.popleft()
        tickets.remove([fr, to])
        answer.append(fr)

        if len(tickets) == 0:
            answer.append(to)

        for i in range(len(tickets)):
            if tickets[i][0] == to:
                q.append([tickets[i][0], tickets[i][1]])
                break

    print( answer)

a = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]

solution(a)