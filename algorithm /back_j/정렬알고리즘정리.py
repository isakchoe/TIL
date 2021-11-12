from collections import deque


arr = [3, 2, 4, 6, 60, 23, 57, 43]


# 삽입정렬
def insert_order(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
            else:
                # 왼쪽은 정렬되어 있기에 아니면, 더 확인할 필요 없다
                break
    return arr


# 버블정렬 -- 삽입정렬과 순서만 반대
def bubble_sort(arr):
    for i in range(len(arr), -1, -1):
        for j in range(1,i):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
    return arr


print(bubble_sort(arr), 'bubble')


# 선택정렬
def select_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 퀵정렬
def quick_sort(arr):
    if len(arr)  <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    # 순차탐색
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    p = end

    i = start
    big = start

    while i < end:
        if my_list[i] > my_list[p]:

            i += 1
        else:
            my_list[i], my_list[big] = my_list[big], my_list[i]
            i += 1
            big += 1

    my_list[p], my_list[big] = my_list[big], my_list[p]
    return big


# 퀵 정렬
def quicksort_origin(my_list, start, end):
    # 코드를 작성하세요.
    if end - start < 1:
        return

    else:
        pivot = partition(my_list, start, end)
        quicksort_origin(my_list, start, pivot - 1)
        quicksort_origin(my_list, pivot + 1, end)


# print(quick_sort(arr))

# 병합정렬

def merge(arr1, arr2):

    a = 0
    b = 0

    answer = []
    # 둘다 안끝남
    while a < len(arr1) and b <len(arr2):
        if arr1[a] > arr2[b]:
            answer.append(arr2[b])
            b+=1
        else:
            answer.append(arr1[a])
            a+=1

    # 둘중하나 끝난경우,
    while a < len(arr1):
        answer.append(arr1[a])
        a+=1

    while b < len(arr2):
        answer.append(arr2[b])
        b+=1

    return answer


def merge_sort(arr):

    if len(arr) <2:
        return arr
    start = 0
    end = len(arr)

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))



# 계수정렬
def count_sort(arr):

    m = max(arr)

    data = [0]*(m+1)

    # o(n)
    for num in arr:
        data[num] +=1

    answer = []

    # o(m)
    for arr_elements, elements_count in enumerate(data):
        if elements_count !=0:
            for n in range(elements_count):
                answer.append(arr_elements)

    return answer


# 위상정렬
def topological_sort(tree):

    # tree ---> [30,1, 30, 2, 30, 3, 3, 4]   루트노드가 30, 자식 노드 3개(1,2,3)   3 -->4자식노드


    #
    # # 위상정렬
    # a 노드 --> B 노드  화살표를 표시하는 것
    #
    # 각 노드마다, 받는 화살표를 기록하자
    #
    # 받는 화살표가 0 이면? --> 루트노드   !! 중요!!
    #
    # 로직 : 화살표가 0인노드를 큐에 넣는다. 루트노드에 연결된 노드: 값 -1  --> 0 인값이 생겨요
    #
    # 쏘는 화살표가 없다 --> 리프노드
    #
    #
    # 루트 ---> 동일레벨노드 ---->하위레벨 노드 --->
    #
    # a ---> b   ---> e
    #        c
    #        d

    # 집합으로 노드 개수 판별
    arr = list(set(tree))
    arr.sort()

    index_dic = {}

    #  값: 인덱스   딕셔너리형태
    for i in range(len(arr)):
        index_dic[arr[i]] = i

    n = len(arr)

    # 인접차수
    indegrees = [0]*(n)

    for i in range(0,len(tree),2):
        a,b = tree[i], tree[i+1]
        b_index = index_dic[b]
        indegrees[b_index] += 1

    q = deque
    for i in range(n):
        if indegrees[i] == 0:
            q.append([i, arr[i]])

    while q:
        now_index, value  = q.popleft()
        print(value)
        for i in range(0,tree,2):
            a, b = tree[i], tree[i+1]
            if a == value:
                b_index = index_dic[b]
                indegrees[b_index] -= 1
                if indegrees[b_index] == 0:
                    q.append([b_index, arr[b_index]])




# print(count_sort(arr))

print(merge_sort(arr), 'merge')



