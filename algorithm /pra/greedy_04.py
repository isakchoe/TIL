
def main2():

    # 책 답안

    s = time.time()

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

    e = time.time()
    print(e-s)





main2()