


arr = [123, 323, 2, 3, 60, 23, 57, 43]


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
    for i in range(len(arr), 0, -1):
        for j in range(1,i):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
    return arr

# 선택정렬
def select_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # swap
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
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

    mid = (start+end)//2

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

# print(count_sort(arr))

print(merge_sort(arr), 'merge')