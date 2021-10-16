


# 입력받기
n, k = map(int, input().split())

arr = list(map(int, input().split()))

max_value = sum(arr[:k])

for i in range(len(arr)-k+1):
    temp = sum(arr[i:i+k])

    if temp > max_value:
        max_value = temp

print(max_value)


