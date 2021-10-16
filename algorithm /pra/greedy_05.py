def main():

    # 볼링공 고르기 문제

    # n^2 시간복잡도

    n,m = map(int, input().split())

    data = list(map(int, input().split()))

    data.sort()


    answer = 0



    for i in range(n-1):
        for e in range(i+1, n):
            if data[i] != data[e]:
                answer += 1

    print(answer)


def a():
    n,m = map(int, input().split())
    data = list(map(int , input().split()))

    arr = [0]*11

    for x in data:
        arr[x] +=1

    result = 0

    for i in range(1,m+1):
        n -= arr[i]
        result += arr[i]*n

    print(result)

a()