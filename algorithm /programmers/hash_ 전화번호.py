

def solution(phone_book):
    answer = True

    dic = {}

    # 길이가 짧은거 앞으로
    phone_book.sort()

    # 순차탐색하면서 딕셔너리에 추가
    for num in phone_book:
        for i in range(1,len(num)+1):
            if num[0:i] in dic:
                return False

        dic[num] = 1



    return answer