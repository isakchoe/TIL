


# 1. 세그먼트 트리 이용!

def solution(n, k, cmd):

    tree = [0]*4*n

    # 상태정보
    arr = [1]*n

    # start, end ==> 전체범위에서 점점 줄여나가는 가변방식

    def init(start, end, node):
        # 구간이 아닌, 특정 노드 출력하는 경우
        if start == end:
            tree[node] = arr[start]
            return tree[node]

        # 구간을 출력하는 경우
        mid = (start+end)//2
        tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
        return tree[node]


    def tree_sum(start, end, node, left, right):
        if left > end or right < start:
            return 0

        # 범위안에 있는 경우
        if left <= start and end <= right:
            return tree[node]

        mid = (start+end)//2

        return tree_sum(start, mid, node*2, left, right) + tree_sum(mid+1, end, node*2+1, left, right)

    def tree_update(start, end, node, index, diff):

        # 범위 벗어나는 경우
        if index <start or end < index:
            return
        # 변동 사항
        tree[node] += diff

        # 재귀 종료
        if start == end:
            return

        mid = (start+end)//2

        # 왼쪽 자식, 오른쪽 자식 탐색
        tree_update(start, mid, node*2, index, diff)
        tree_update(mid+1, end, node*2+1, index, diff)


    # 트리 생성
    init(0,n-1,1)


    now_num = k

    delete_stack = []

    for command in cmd:
        # print(now_num)
        if command[0] == 'D':
            l = now_num
            r = n-1

            while l <= r :
                mid = (l+r)//2

                # now_num 부터 mid 지점까지 구간합
                temp = tree_sum(0, n-1, 1, now_num, mid)

                if temp-1 >= int(command[2]):
                    r = mid -1
                else:
                    l = mid +1

            now_num = l



        elif command[0] == 'U':
            l = 0
            r = now_num

            while l <= r:
                mid = (l + r) // 2

                # now_num 부터 mid 지점까지 구간합
                temp = tree_sum(0, n-1, 1, mid, now_num)
                # print('u', temp, l, mid, r, now_num, arr, int(command[2]))

                if temp - 1 >= int(command[2]):
                    l = mid + 1
                else:
                    r = mid - 1

            now_num = r




        elif command == 'C':
            arr[now_num] = 0
            tree_update(0,n-1, 1, now_num, -1)
            delete_stack.append(now_num)

            pivot = 0
            l = now_num
            r = n-1

            # now_num 재설
            while l <= r :
                mid = (l+r)//2

                # now_num 부터 mid 지점까지 구간합
                temp = tree_sum(0, n-1, 1, now_num, mid)

                if temp >= 1:
                    r = mid -1
                    if temp == 1:
                        pivot += 1
                else:
                    l = mid +1

            now_num = l

            if pivot ==0:
                l = 0
                r = now_num

                while l <= r:
                    mid = (l + r) // 2

                    # now_num 부터 mid 지점까지 구간합
                    temp = tree_sum(0, n - 1, 1, mid, now_num)

                    if temp >= 1:
                        l = mid + 1
                    else:
                        r = mid - 1

                now_num = r





        elif command == 'Z':
            temp = delete_stack.pop()
            arr[temp] = 1

            # 구간합 변경
            tree_update(0,n-1, 1, temp, 1)




    # 출력
    answer = ""
    for num in arr:
        if num == 1:
            answer += 'O'
        else:
            answer += 'X'

    return answer


cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(8,2,cmd))

