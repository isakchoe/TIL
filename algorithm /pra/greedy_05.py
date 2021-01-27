def main():

    # 볼링공 고르기 문제

    n,m = map(int, input().split())

    data = list(map(int, input().split()))

    answer = 0

    for i in range(n-1):
        for e in range(i+1, n):
            if data[i] != data[e]:
                answer += 1

    print(answer)


main()