#
# n = int(input())
#
# data=[]
#
#
#
# for i in range(n):
#     temp = int(input())
#     data.append(temp)
#
# data.sort()
#
# total = 0
# prev = data[0]
#
# for i in range(1,n):
#     total += prev + data[i]
#     prev = prev + data[i]
#
# print(total)

# 틀렸어!!! 문제 이해를 다시하기를,,,


import  heapq

n = int(input())

heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)


total = 0

while len(heap) !=1 :

    first = heapq.heappop(heap)
    sec = heapq.heappop(heap)

    sum_value = first + sec

    total += sum_value

    heapq.heappush(heap,sum_value)

print(total)















