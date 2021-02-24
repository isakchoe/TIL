
n = int(input())

data=[]

for i in range(n):
    temp = int(input())
    data.append(temp)

data.sort()

total = 0
prev = data[0]

for i in range(1,n):
    total += prev + data[i]
    prev = prev + data[i]

print(total)