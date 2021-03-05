
from bisect import  bisect_left, bisect_right

# left ~ right  범위 값 개수!!
def count_by_range(arr, left, right):

    

    left_index = bisect_left(arr, left)
    right_index = bisect_right(arr, right)

    return right_index - left_index



def main():
    n , x = map(int, input().split())

    data = list(map(int, input().split()))

    # data 함수에 x 값이 있냐 확인!
    a = count_by_range(data, x,x)

    if a == 0:
        print(-1)
    else:
        print(a)










if __name__ == "__main__":
    main()