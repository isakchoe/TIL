

# 유니언파인드
#  집합 따로 저장 !
# -----------밑에 작업 안해도 된다!!------
# for 문 돌면서, 모든 루트 노드 갱신 작업  -- O(N)
#  for 문 돌면서, 같은 루트 노드 카운팅  -- O(N)

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_p(parent,a)
    b = find_p(parent, b)

    if a > b:
        parent[a] = b
        set_lens[b] += set_lens[a]
    else:
        parent[b] = a
        set_lens[a] += set_lens[b]



t = int(input())

# 부모계수 세팅
parent = [0]*(10**6 +1)
for i in range(len(parent)):
    parent[i] = i

# 같은 집합 내 요소 개수 저장하는 리스트
set_lens = [1] *(10**6 +1)


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
        # 타켓의 루트 노드
        target = find_p(parent, int(command[1]))

        print(set_lens[target])






