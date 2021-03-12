
def main():
    n = int(input())
    arr = list(map(int,input().split()))

    arr.reverse()

    dp = [1]*n

    for i in range(1,n):

        for e in range(0,i):
            if arr[i] > arr[e]:
                # 점화식
                dp[i] = max(dp[e]+1,dp[i])

    print(n - max(dp))



main()





