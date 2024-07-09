
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


max_count = -1
min_count = int(1e9)

def dfs(num, count):
    global max_count, min_count
    now_count = count_odd(num)
    if len(num) == 1:
        return now_count + count
    elif len(num) == 2:
        temp = int(num[0]) + int(num[1])
        return dfs(str(temp), count + now_count)
    else:
        for i in range(len(num)-2):
            for j in range(i+1, len(num)-1):
                front = num[0:i+1]
                middle = num[i+1: j+1]
                back = num[j+1:]
                # print(front,middle,back)
                total = int(front) + int(middle) + int(back)
                temp = dfs(str(total), now_count + count)

                max_count = max(max_count, temp)
                min_count = min(min_count, temp)
        # 리턴이 없으면, temp = null
        return temp



if len(n) <= 2:
    answer = dfs(n, 0)
    print(answer, answer)
else:
    dfs(n,0)
    print(min_count, max_count)