
# 입력받기
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


stack = []
next_number = 1

answer = []
flag = True

# 첫번째까지 넣기
for i in range(1,arr[0]+1):
    stack.append(i)
    answer.append('+')
    next_number = i+1
stack.pop()
answer.append('-')

for i in range(1,len(arr)):
    # print(stack)
    now = arr[i]

    # now 가 스택에 있는 경우
        #     top 에 잇는경우 가능
        #     top 이 아니라면 불가

    # 스택에 들어간적 있는 경우
    if next_number-1 >= now:
        if stack[-1] == now:
            stack.pop()
            answer.append('-')
        else:
            flag = False
            break

    # 스택에 들어간적 없는  경우
    elif next_number-1 <now:
        # 해당 수까지 스택에 넣고
        for j in range(next_number, now+1):
            stack.append(j)
            answer.append('+')


        next_number = now+1
        # 원하는 요소 출력
        stack.pop()
        answer.append('-')



if flag:
    for i in answer:
        print(i)
else:
    print('NO')



