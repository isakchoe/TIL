

def solution(n):
    # 3진법 변환 문제

    temp =""

    while n >3:
        if n%3 == 0:
            temp = "4" + temp
            n = n//3 -1

        else:
            temp = str(n%3) + temp
            n = n//3

    if n == 3:
        temp = "4" + temp
    else:
        temp = str(n) + temp

    return temp


n = 15

if __name__ == '__main__':
    print(solution(n))