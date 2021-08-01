
# 미드값 비교를 통한 구현


n = int(input())

num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

front_mid  = num_list[0]
mid = num_list[0]
back_mid = num_list[0]

for i in range(len(num_list)):

    target = num_list[i]

    # 주어진 값이 미드랑 같은 경우
    if num_list[i] == mid:
        print(num)
        back_mid = mid
        continue


    # 짝수
    if i%2 == 0:
        if target > mid:
            if target > back_mid:
                front_mid  = mid
                mid = back_mid
                back_mid = ?


