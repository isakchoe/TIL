
# 입력
n = input()

# brute force??
# 3자리 이상 --> 여러 경우의 수   콤마 2개 찍기


def count_odd(num):
    count = 0
    for s in num:
        if int(s)%2 == 1:
            count+= 1
    return count


answer = 0

def dfs(num, count):

    count += count_odd(num)

    if len(num) == 1:
        return count
    elif len(num) == 2:
        temp = int(num[0])+ int(num[1])
        return dfs(str(temp))


def solution(num, count):

    if len(num) <=2:
        return dfs(num, count)
    else:

        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                front = int(num[0:i + 1])
                middle = int(num[i + 1: j + 1])
                back = int(num[j + 1:])

                total_sum = front + middle + back
                temp = count_odd(str(total_sum))

                return temp + solution(total_sum, count+ temp)





