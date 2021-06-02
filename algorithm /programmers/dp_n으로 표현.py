

def solution(N, number):


    # dp 테이블
    dp = [[] for _ in range(9)]

    # 연산이 아닌 것, N NN NNN NNNN NNNNN 등 미리 넣어주기
    for i in range(1, 9):
        if number == int(str(N) *i):
            return i
        dp[i].append(int(str(N)*i))


    for i in range(2,9):
        # (1,h-1), (2,h-2) ......
        for h in range(1, i//2 +1):
            for s in range(len(dp[h])):
                # 기준값
                now = dp[h][s]
                for j in range(len(dp[i-h])):
                    # 현재값
                    temp = dp[i-h][j]

                    # 기준값 현재값 사칙연산 시작~

                    multi = now * temp
                    add = now + temp

                    # 나눗셈 앞,뒤
                    if temp != 0:
                        divide = now//temp
                    if now != 0:
                        divide2 = temp//now

                    # 마이너스 2개
                    minus = temp - now
                    minus2 = now - temp

                    # 찾고자 하는 수면 바로 리턴
                    if number in [add, multi, minus2, minus, divide2, divide]:
                        return i


                    # 연산결과 삽입
                    dp[i].append(multi)
                    dp[i].append(add)
                    if temp !=0 :
                        dp[i].append(divide)
                    if now != 0:
                        dp[i].append(divide2)

                    dp[i].append(minus)
                    dp[i].append(minus2)


    # 위에서 다 걸르기 때문에 필요 없는 코드!

    # for i in range(1,9):
    #     for j in range(len(dp[i])):
    #         if dp[i][j] == number:
    #             return i



    # 중요 포인트!!
    # 전부다 작업을 수행하고 출력 vs 탐색 중간에 발견하면 break
    #   시간 길다    vs 짧다
    #    정확성  VS 예외처리에서 실수 가능성
    # 시간 차이가 크지 않다면,, 정확성을 먼저 추구!! 


    return -1