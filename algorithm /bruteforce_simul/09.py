

# 2번째 풀이,, 해답 안보고 ! 

def compress(char, num):

    result = ''
    count = 1

    for i in range(0,len(char),num):
        temp = char[i:i+num]

        # 다음 단어랑 같은경우, count 증가해주고 스킵
        if temp == char[i+1:i+num]:
            count += 1
            continue
        # 현재 단어가 다음 단어랑 다를 경우, result 에 추가하고 새로 갱신
        else:
            if count == 1 :
                result += temp
            else:
                result += str(count) + temp
                count = 1


    return len(result)


def solution(s):
    answer = len(s)

    half = len(s) // 2 + 1

    for i in range(1, half):

        answer = min(compress(s, i), answer)

    return answer