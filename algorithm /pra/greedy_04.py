from itertools import combinations
import  time

def main():



    n = int(input())
    data = list(map(int, input().split()))

    if min(data)!= 1:
        print(1)


    blank =[]

    for i in range(1,n+1):
        result = list(combinations(data,i ))
        for e in result:
            temp = sum(e)
            if temp not in blank:

                blank.append(temp)

    blank.sort()

    answer = 0

    for i in range(len(blank)):
        if blank[i] != i+1:
            print(blank[i-1] +1)
            break



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








main()
main2()