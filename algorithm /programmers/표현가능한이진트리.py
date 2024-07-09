


from collections import  deque

def make_binary_num(num):
    q = deque()
    while num != 1:
        if num%2 == 0:
            q.appendleft("0")
        else:
            q.appendleft("1")
        num = num//2
    q.appendleft("1")

    n = 1
    while True:
        if len(q) >= 2**n:
            n+=1
        else:
            temp = 2**n -1 - len(q)
            for _ in range(temp):
                q.appendleft("0")
            break

    return ''.join(q)

def solution(numbers):
    answer = []
    for num in numbers:
        binary_num = make_binary_num(num)
        if check(binary_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def check(binary_num):
    n = len(binary_num)

    if n == 1:
        return True

    left = binary_num[:n // 2]
    right = binary_num[n // 2 + 1:]

    # 루트.. 중간 확인 !
    # 0 이면, 좌우 모두 0 으로만...
    if binary_num[n//2] == "0":
        return binary_num.count('0') == n

    if check(left) == False or check(right) == False:
        return False
    return True



print(solution([3,7, 42, 5,10000000000000, 1, 27]))
