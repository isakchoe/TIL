
# 각 명령마다 함수로 만들기
# 입력받고, 명령 수행
# 계산

import sys
input = sys.stdin.readline


def sit_down(i,x):
    # x 는 -1 해서 받기
    train_list[i][x-1] = 1

def stand_up(i,x):
    train_list[i][x-1] = 0

def move_back(i):
    for index in range(19,0,-1):
        train_list[i][index] = train_list[i][index-1]
    # 맨앞 처리
    train_list[i][0] = 0

def move_forward(i):
    for index in range(19):
        train_list[i][index] = train_list[i][index+1]
    # 맨뒤 처리
    train_list[i][19] = 0


# 입력
n,m = map(int, input().split())

# 기차 리스트
train_list = [[0]*20 for _ in range(n+1)]

# 명령수행
for _ in range(m):
    command = tuple(map(int, input().split()))

    if command[0] == 1:
        i = command[1]
        x = command[2]
        sit_down(i,x)
    elif command[0] == 2:
        i = command[1]
        x = command[2]
        stand_up(i,x)
    elif command[0] == 3:
        i = command[1]
        move_back(i)
    else:
        i = command[1]
        move_forward(i)


# 탐색
train_dic = {}
total = 0

for i in range(1,n+1):
    temp = map(str, train_list[i])
    temp_key = ''.join(temp)

    if temp_key not in train_dic:
        train_dic[temp_key] = 1
        total += 1
print(total)

in

# 첫번째 실수,,, 인덱스 20,19,,,, 개수랑 번호수 조율하는거 중요
# 두번재실수, 입력값 split, 자리수로 해서 index, value error
# 세번쩨,  0번째 기차는 포함되지 않아야 하는데 포함시켰다.

# 세번째 ==> import sys 로 해결