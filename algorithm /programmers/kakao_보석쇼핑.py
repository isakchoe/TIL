

def solution(gems):
    # 투포인터!!
    # start, end 로 시작
    # 모든 종류 담을때까지 End 증가
    # 만족하면 start 증가
    # 최소 범위 구하기,,  ==> start, end 끝 도달할때 까지 반복!!
    # 해쉬 ==> 딕셔너리 이용!!!


    #

    # 보석 종류 개수
    n = len(set(gems))

    # 투포인터
    start = 0
    end = 0

    # 보석 개수 딕셔너리 이용
    dic = {}
    dic[gems[end]] = 1

    # 정답, 비교를 위한 피벗
    answer = [0,0]
    pivot = len(gems)+1

    # 반복문
    while start != len(gems):
        # 종류 충족 하지 못하면
        if len(dic) != n:
            # end 가 끝이 아니면 증가
            if end != len(gems)-1:
                end += 1
                # 내 딕셔너리에 추가 혹은 더하기
                if gems[end] not in dic:
                    dic[gems[end]] = 1
                else:
                    dic[gems[end]] += 1

            # end 가 끝인데, 조건 충족 못하면 break
            else:
                break
        # 충족하면 start 증가
        else:
            # 최소 길이인지 비교
            if end - start < pivot:
                answer[0] = start +1
                answer[1] = end + 1
                pivot = end - start
            # 내 딕셔너리에서 빼기
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1

    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

if __name__ == '__main__':
    print(solution(gems))