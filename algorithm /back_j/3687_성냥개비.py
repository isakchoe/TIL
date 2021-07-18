


# test case
t = int(input())

for tc in range(t):
    # 성냥개수
    n = int(input())

    # 최대값 구하기 , 짝수 ==> 1111 형식 홀수 7111 형식

    length = n//2
    max_result = int('1'*length)

    # 홀수일때 최대값
    if n%2 != 0:
        temp = '7'
        temp += '1'*(length-1)

        max_result = int(temp)


    # 최소값 구하기, 7로 나누기 (자리수를 최대한 늘리지 않기 위해)
    min_result = 0

    # dp 테이블
    dp = [0,0,1,7,4,2,6,8,10,18,22]

    # 11보다 작을경우
    if n <11:
        min_result = dp[n]

    # 7로 나누어서 나머지 확인
    else:
        # 몫
        quotient = n//7

        # 나머지가 0 이면
        if n%7 == 0:
            min_result = int('8'*(quotient))

        # 나머지 1
        elif n%7 == 1:
            min_result = int('10' + (quotient-1)*'8')

        # 나머지 2
        elif n%7 == 2:
            min_result = int('1' +  (quotient * '8'))

        elif n%7 == 3:
            min_result = int('200'+ ((quotient-2)*'8'))

        elif n%7 == 4:
            min_result = int('20' + (quotient-1)*'8')

        elif n%7 == 5:
            min_result =  int('2' + quotient*'8')
        else:
            min_result = int('6' + (quotient)*'8')


    print(min_result, max_result)

    