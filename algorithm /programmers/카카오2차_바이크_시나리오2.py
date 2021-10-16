





import requests


base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

header = {'X-Auth-Token':'35028b824899be5d3b577fa41988f32a'
           }
data = '''
{
         "problem": 2
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





matrix = [ [0]*60 for i in range(60)]
count = 0
for j in range(60):
    for i in range(59,-1,-1):
        matrix[i][j] = count
        count += 1



def dic_loca(id):

    col = id//60
    rest = id%60
    row = 59 - rest

    return [row,col]


time = 1




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
    for i in range(10):
        bike_id, bike_count = bike_list[i]

        bike_row, bike_col = dic_loca(bike_id)


        # 가까운 트럭 찾기

        pivot = 400
        min_row = 0
        min_col = 0
        pivot_id = 0

        for truck_id, truck_loca in truck_list:
            truck_row, truck_col = dic_loca(truck_loca)

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


            if 0<=mid_row<10 and 0<=mid_col<10:
                temp_id = matrix[mid_row][mid_col]

                for bike_id, count in bike_list:
                    if bike_id == temp_id:
                        if count > mid_pivot:
                            pivot_row = mid_row
                            pivot_col = mid_col
                            mid_pivot = count


        # min(트럭) --> pivot --> bike

        command = []

        if min_row > pivot_row:
            count = min_row - pivot_row
            for i in range(count):
                command.append(1)

        elif min_row < pivot_row:
            count = pivot_row - min_row
            for i in range(count):
                command.append(3)

        count = abs(min_col-pivot_col)
        if min_col < pivot_col:
            for i in range(count):
                command.append(2)
        elif min_col > pivot_col:
            for i in range(count):
                command.append(4)


        pick = mid_pivot//2

        for i in range(pick):
            command.append(5)

        if bike_row > pivot_row:
            count = bike_row - pivot_row
            for i in range(count):
                command.append(3)

        elif bike_row < pivot_row:
            count = pivot_row - bike_row
            for i in range(count):
                command.append(1)

        count = abs(bike_col - pivot_col)
        if bike_col < pivot_col:
            for i in range(count):
                command.append(4)
        elif bike_col > pivot_col:
            for i in range(count):
                command.append(2)


        for i in range(pick):
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
