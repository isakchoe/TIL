
def main():
    n = int(input())
    arr = list(map(int,input().split()))


    count = 0
    end = arr[-1]

    for i in range(n-2,-1,-1):
        if arr[i] >= end:
            end = arr[i]
        else:
            count+=1


    print(count)


main()





