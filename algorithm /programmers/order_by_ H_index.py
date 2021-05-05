

def solution(citations):
    citations.sort()
    # h 인덱스 최대값
    answer = len(citations)

    for i in citations:
        if i < answer:
            answer -= 1
        # 뒤는 모두 큰 수라서 탐색할 필요 없다.
        else:
            break

    return answer