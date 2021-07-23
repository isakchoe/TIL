
# 각 명령마다 함수로 만들기
# 입력받고, 명령 수행
# 계산


def sit_down(i,x):
    train_list[i][x-1] = 1

def stand_up(i,x):
    train_list[i][x-1] = 0

def move_back(i):

    for index in range(19,0,-1):
        train_list[i][index] = train_list[i][index-1]
    train_list[i][0] = 0

def move_forward(i):
    for index in range(19):
        train_list[i][index] = train_list[i][index+1]

    train_list[i][19] = 0

# 입력
n,m = map(int, input().split())

# 기차 리스트
train_list = [[0]*20 for _ in range(n+1)]

# 명령수행
for _ in range(m):
    command = input()

    i = int(command[2])

    if command[0] == '1':
        x = int(command[4])
        sit_down(i,x)
    elif command[0] == '2':
        x = int(command[4])
        stand_up(i,x)
    elif command[0] == '3':
        move_back(i)
    else:
        move_forward(i)


print(train_list)


# 탐색
total = 0

train_dic = {}

for train in train_list:
    temp = map(str, train)
    temp_key = ''.join(temp)

    if temp_key not in train_dic:
        train_dic[temp_key] = 1
        total += 1

print(total)