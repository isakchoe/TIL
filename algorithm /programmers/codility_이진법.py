

# 이진법 만들기
def make(num):
    temp = ""
    while num != 1:
        temp  = str(num %2) + temp
        num = num//2

    temp = "1" + temp
    return temp

def solution(N):
    # 이진법 변환
    bi = make(N)
    max_result = 0
    count = 0

    for i in range(len(bi)):

        if bi[i] == "1":
            # 맥스값이랑 비교
            if count > max_result:
                max_result = count
            # 카운트는 무조건 갱신!!
            count = 0
        else:
            count += 1

    return max_result

