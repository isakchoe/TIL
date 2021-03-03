
def bi_sect(arr,start,end, target):

    while start <=end:
        mid = (start + end)//2

        if arr[mid] == target:
            return [start, end]

        elif arr[mid] > target:
            end = mid -1

        elif arr[mid] < target:
            start = mid + 1

    return -1



def main():
    n , x = map(int, input().split())

    data = list(map(int, input().split()))


    if bi_sect(data,0,len(data)-1, x) == -1:
        print(-1)

    else:
        count = 0
        start, end = bi_sect(data,0,len(data)-1 ,x)

        for i in range(start,end+1):
            if data[i] == x:
                count += 1

        print(count)





if __name__ == "__main__":
    main()