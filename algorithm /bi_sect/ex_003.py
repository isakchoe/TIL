

def main():

    n,m = map(int, input().split())

    data = list(map(int, input().split()))

    start = 0
    end = max(data)


    result = 0

    while (start <=end):
        mid = (start+end)//2

        total = 0
        for x in data:
            if mid < x:
                total += x - mid

        if total < m:
            end = mid - 1

        else:
            start = mid + 1
            result = mid

    print(result)



main()