

def main():

    n = int(input())

    arr = list(map(int, input().split()))

    arr.sort()

    print(arr[(n-1)//2])







if __name__ == '__main__':
    main()
