

# input
n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

l1, r1 = map(int, input().split())
l2, r2 = map(int, input().split())


def attack(row, col):
    for i in range(row-1, col):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                break


def get_sum():
    total = 0
    for i in range(n):
        total += sum(matrix[i])
    return total


attack(l1, r1)
attack(l2, r2)

answer = get_sum()

print(answer)

