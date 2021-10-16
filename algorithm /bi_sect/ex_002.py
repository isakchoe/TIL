
def bi_sect(arr, target,  start, end):

    if start > end:
        return False

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            start = mid+1

        elif arr[mid] > target:
            end = mid - 1

    return False







def main():
    n = int(input())
    data = list(map(int, input().split()))

    m = int(input())
    c_order = list(map(int, input().split()))

    data.sort()

    for i in range(len(c_order)):
        if bi_sect(data, c_order[i], 0, n-1):
            print("yes", end = " ")
        else:
            print("no", end = " ")



if __name__ == "__main__":
    main()