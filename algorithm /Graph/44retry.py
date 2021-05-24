
def find_p(p,x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]

def uni(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)

    if a > b:
        p[a] = b
    else:
        p[b] = a



# 입력받기
n = int(input())

x_list =[]
y_list = []
z_list = []

for i in range(n):
    x,y,z = map(int, input().split())

    x_list.append((x,i+1))
    y_list.append((y, i+1))
    z_list.append((z, i+1))

# 정렬
x_list.sort()
y_list.sort()
z_list.sort()


answer = []

for i in range(1,n):
    # 거리 값
    temp = abs(x_list[i][0] - x_list[i-1][0])
    temp2 = abs(y_list[i][0] - y_list[i-1][0])
    temp3 = abs(z_list[i][0] - z_list[i-1][0])


    # 거리값, i, i-1 노드 삽입
    answer.append((temp, x_list[i][1], x_list[i-1][1]))
    answer.append((temp2, y_list[i][1], y_list[i - 1][1]))
    answer.append((temp3, z_list[i][1], z_list[i - 1][1]))


# answer 정렬
answer.sort()

parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

total = 0

for i in range(len(answer)):
    # 노드 번호 a,b  그리고 a-b 사이 거리값
    a = answer[i][1]
    b = answer[i][2]
    dis = answer[i][0]

    # 루트 다르면, 합집합
    if find_p(parent,a) != find_p(parent,b):
        uni(parent,a,b)
        total += dis

# 출력
print(total)


