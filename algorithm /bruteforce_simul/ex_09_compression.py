def solution(s):
    # 프로그래머스 카카오 문자열 압축


    # 압축전 값 (길이 1인경우도 포함)
    answer = len(s)


    # 문자열 길이 절반까지만 탐색 (절반을 넘으면 중복이 없기 때문에!)

    for step in range(1, len(s)//2 + 1):
        prev = s[0:step]
        count = 1

        compressed = ''
        for j in range(step, length, step):
            if prev == s[j: j + step]:
                count += 1

            else:
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                count = 1

        compressed += str(count) + prev if count > 1 else prev

        answer = min(answer, len(compressed))

    return answer

