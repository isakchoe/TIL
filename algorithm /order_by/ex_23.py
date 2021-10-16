
n = int(input())

blank = []

for i in range(n):
    name, lang, eng, math = input().split()

    blank.append((name, int(lang), int(eng), int(math)))

blank.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(blank[i][0])

