
import sys

input = sys.stdin.readline


# 플로이드워셜
# a,b,c ==> 숫자 인덱스 매핑만 잘 해주기


n = int(input())

INF = int(1e9)

# 그래프
data = [[INF]*(26) for _ in range(26)]

# 알파벳 매핑위한 딕셔너리
# dic = {'a':0, 'b': 1, "c": 2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, 'k':10, "l":11, "m":12, "n":13, "o":14, "p":15,
#        "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

dic = {k:v for v,k in enumerate("abcdefghijklmnopqrstuvwxyz")}

for _ in range(n):
    first, iss, last = input().split()

    # 숫자매핑
    first = dic[first]
    last = dic[last]

    data[first][last] = 1

# 플로이드 워셜
for k in range(26):
    for i in range(26):
        for j in range(26):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

m = int(input())

# 출력
for _ in range(m):
    f, iss, l = input().split()

    f = dic[f]
    l = dic[l]

    if data[f][l] != INF:
        print("T")
    else:
        print("F")
