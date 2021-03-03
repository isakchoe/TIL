

def bi_sect(arr, start, end):

    while start <=end:
        mid = (start+end)//2

        if arr[mid] == mid :
            return mid

        elif arr[mid] > mid:
            end = mid -1

        else:
            start = mid + 1

    return -1


def main():
    n = int(input())

    data = list(map(int, input().split()))

    answer =  bi_sect(data, 0, len(data)-1)

    print(answer)


if __name__ == '__main__':
    main()
