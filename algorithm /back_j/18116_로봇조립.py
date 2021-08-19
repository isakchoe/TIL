
import sys
input = sys.stdin.readline

# 유니언파인드
#  집합 따로 저장 !

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_p(parent,a)
    b = find_p(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a



t = int(input())

# 부모계수 세팅
parent = [0]*(10**6 +1)
for i in range(len(parent)):
    parent[i] = i


# 카운트 딕
dic = {}


# 입력받기
for _ in range(t):
    command = input().split()

    # i 명령인지, q 인지 확인
    if command[0] == "I":
        a = int(command[1])
        b = int(command[2])

        if find_p(parent,a) != find_p(parent, b):
            union(parent, a, b)



    else:
        # 부모계수 갱신
        for i in range(1, len(parent)):
            find_p(parent, i)

        target = parent[int(command[1])]

        count = 0
        for i in range(1,len(parent)):
            if parent[i] == target:
                count += 1
        print(count)




