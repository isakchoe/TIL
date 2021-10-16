

def solution(A, K):
    # 예외 처리
    if len(A) == 0:
        return A
    for i in range(K):
        back = A.pop()
        A.insert(0,back)

    return A
