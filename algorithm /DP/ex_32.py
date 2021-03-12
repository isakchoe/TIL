

n = int(input())

arr=[]

for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)


for i in range(1,n):
    for e in range(len(arr[i])):

        if e-1 >=0:
            left = arr[i-1][e-1]
        else:
            left = arr[i-1][e]
        if e <len(arr[i-1]):
            right = arr[i-1][e]
        else:
            right = arr[i-1][e-1]

        # 점화식
        arr[i][e] += max(left,right)

result = 0
for i in range(n):
    result = max(result, arr[n-1][i])


print(result)

