

n = int(input())

arr = list(map(int, input().split()))




answer = int(1e9)

for i in range(len(arr)-2):



    a = arr[i]
    b = arr[i+1]
    c = arr[i+2]



    total = 0

    total += abs(a-b)
    total += abs(b-c)
    total += abs(c-a)


    if total < answer:
        answer = total

print(answer)

