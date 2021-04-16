
def main2():

    # 책 답안


    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    target = 1

    for i in data:
        if i <=target:
            target += i
        else:
            break

    print(target)







main2()