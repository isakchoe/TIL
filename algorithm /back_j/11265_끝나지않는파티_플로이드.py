
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])


for _ in range(m):
    a, b, c = map(int, input().split())

    if data[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")