

def solution(expression):
    # 연산자 3개    경우의 수는 최대 6
    # 스택 이용 !!
    #  하나의 경우의 수 ==> 백만 , 총 600만

    # parsing
    raw = []
    temp = ""

    for i in range(len(expression)):
        if expression[i] != "*" and expression[i] != "+" and expression[i] != "-":
            temp += expression[i]
        else:
            raw.append(int(temp))
            raw.append(expression[i])
            temp = ""

    raw.append(int(temp))

    oper = ["+", "-", "*"]

    # print(raw)
    answer =  []

    # 경우의 수   ==> 실수가 너무 많았다, 변수명!! pop 실수, for 구문 실수 등등 실수가 많을 로직
    # print 찍어가면서 구현
    for i in range(3):

        s = [raw[0]]
        # 1차 계산
        for n in range(1, len(raw)):
            if s[-1] == oper[i]:
                s.pop()
                a = s.pop()

                # 연산 기호 확인
                if oper[i] == "+":
                    s.append(a + raw[n])
                elif oper[i] == "*":
                    s.append(a * raw[n])
                else:
                    s.append(a - raw[n])
            else:
                s.append(raw[n])


    #     2차 계산
        for j in range(3):
            if i != j:
                s2 =  [s[0]]
                for m in range(1, len(s)):
                    if s2[-1] == oper[j]:
                        s2.pop()
                        b = s2.pop()

                        if oper[j] == "+":
                            s2.append(b + s[m])
                        elif oper[j] == "*":
                            s2.append(b * s[m])
                        else:
                            s2.append(b - s[m])
                    else:
                        s2.append(s[m])

                # print(s2)

                # 계산 완료
                if len(s2) == 1:
                    answer.append(abs(s2[0]))

                elif len(s2) == 3:
                    temp = 0
                    if s2[1] == "+":
                        temp = s2[0] + s2[2]
                    elif s2[1] == "-":
                        temp = s2[0] - s2[2]
                    else:
                        temp = s2[0] * s2[2]
                    answer.append(abs(temp))

                else:
                    total = s2[0]
                    for e in range(2,len(s2),2):
                        if s2[1] == "+":
                            total += s2[e]
                        elif s2[1] == "-":
                            total -= s2[e]
                        else:
                            total *= s2[e]

                    answer.append(abs(total))
    # print(answer)
    return max(answer)



expression =  "200-300-500-600*40+500+500"
if __name__ == '__main__':
    print(solution(expression))