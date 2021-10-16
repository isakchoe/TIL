def main():

    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    answer = 0

    count = 0

    # count = 누적 사람 수 (중간에 초기화 가능)

    for fear in data:
        count += 1

        if count >= fear :
            answer += 1
            count = 0

    print(answer)




main()