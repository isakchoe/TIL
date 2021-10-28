



import requests


base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

header = {'X-Auth-Token':'e01a7b470f7f625b5fe6f719c1e0b07b'
           }
data = '''
{
         "problem": 1
     }
'''

response = requests.post('https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/start',headers=header, data=data)

data = response.json()


auth_key = data['auth_key']

print(auth_key)


fixed_auth_key = auth_key


# location api

fixed_header = {
    'Authorization':fixed_auth_key,
}





matrix = [ [0]*5 for i in range(5)]
count = 0
for j in range(5):
    for i in range(4,-1,-1):
        matrix[i][j] = count
        count += 1


dic_loca = {

    0:[4,0],
    1:[3,0],
    2:[2,0],
    3:[1,0],
    4:[0,0],
    5:[4,1],
    6:[3,1],
    7:[2,1],
    8:[1,1],
    9:[0,1],
    10:[4,2],
    11: [3,2],
    12: [2, 2],
    13: [1, 2],
    14: [0, 2],
    15: [4, 3],
    16: [3, 3],
    17: [2, 3],
    18: [1, 3],
    19: [0, 3],
    20: [4, 4],
    21: [3, 4],
    22: [2, 4],
    23: [1, 4],
    24: [0, 4],

}
time = 1




# 문제 꼼꼼히 읽기
# 주석 쓰면서 풀기
# 변수명 무조건 길게!!






while True:

    # 바이크 위치
    bike_data = requests.get(base_url+'/locations', headers=fixed_header).json()

    bike_locations = bike_data['locations']

    # 바이크 리스트
    bike_list = []

    for bike in bike_locations:
        bike_list.append([bike['id'], bike['located_bikes_count']])

    # 남은 자전거 순으로 정렬, 오름차순
    bike_list.sort(key=lambda  x:x[1])


    truck_data = requests.get(base_url+'/trucks', headers=fixed_header).json()
    truck_list = []
    for truck in truck_data['trucks']:
        truck_list.append([truck['id'], truck['location_id']])


    pivot_dic = {}
    commands = []
    for i in range(5):
        bike_id, bike_count = bike_list[i]

        bike_row, bike_col = dic_loca[bike_id]


        # 가까운 트럭 찾기

        pivot = 400
        min_row = 0
        min_col = 0
        pivot_id = 0

        for truck_id, truck_loca in truck_list:
            truck_row, truck_col = dic_loca[truck_loca]

            distance = abs(bike_row-truck_row) + abs(bike_col - truck_col)

            if distance < pivot and truck_id not in pivot_dic:
                pivot = distance
                min_row = truck_row
                min_col = truck_col
                pivot_id = truck_id

        pivot_dic[pivot_id] = 1


        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        pivot_row = 0
        pivot_col = 0
        mid_pivot = -10

        for j in range(4):
            mid_row = bike_row + dx[j]
            mid_col = bike_col + dy[j]
            # print(mid_row, mid_col, 'mid_row_col')


            if 0<=mid_row<5 and 0<=mid_col<5:
                temp_id = matrix[mid_row][mid_col]

                for bike_id, count in bike_list:
                    if bike_id == temp_id:
                        if count > mid_pivot:
                            pivot_row = mid_row
                            pivot_col = mid_col
                            mid_pivot = count


        # 현위치 --> pivot --> bike

        command = []

        if min_row > pivot_row:
            step1 = min_row - pivot_row
            for _ in range(step1):
                command.append(1)

        elif min_row < pivot_row:
            step2 = pivot_row - min_row
            for _ in range(step2):
                command.append(3)


        if min_col < pivot_col:
            step3 = pivot_col - min_col
            for _ in range(step3):
                command.append(2)
        elif min_col > pivot_col:
            step4 = min_col - pivot_col
            for _ in range(step4):
                command.append(4)


        pick = mid_pivot//2

        for _ in range(pick):
            command.append(5)

        # print(abs(bike_row-pivot_row), abs(bike_col-pivot_col), '확인')
        if bike_row > pivot_row:
            # step5 = bike_row - pivot_row
            # for _ in range(step5):
                # print('아래삽입', pivot_id)
            command.append(3)

        elif bike_row < pivot_row:
            # step6 = pivot_row - bike_row
            # for _ in range(step6):
                # print('위 삽입', pivot_id)
            command.append(1)

        # step = abs(bike_col - pivot_col)
        # print(step, '차이')
        if bike_col < pivot_col:
            # step7 = pivot_col - bike_col
            # for _ in range(step7):
                # print('left',pivot_id)
            command.append(4)
        elif bike_col > pivot_col:
            # step8 = bike_col - pivot_col
            # for _ in range(step8):
                # print('right',pivot_id)
            command.append(2)


        for _ in range(pick):
            command.append(6)


        while len(command) >10:
            command.pop()


        temp = {}
        temp['truck_id'] = pivot_id
        temp['command'] = command

        commands.append(temp)



    para ={
        'commands':
            commands
    }

    # print(commands)

    simulate_data = requests.put(base_url+'/simulate', headers= fixed_header, json=para).json()

    print(simulate_data)

    if simulate_data['status'] == 'ready':
        print(time)
        time+=1
    else:
        break





# score api

score_data = requests.get(base_url+'/score', headers=fixed_header).json()
print(score_data)
