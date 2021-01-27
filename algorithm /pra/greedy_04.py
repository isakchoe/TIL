from itertools import combinations

def main():

    n = int(input())
    data = list(map(int, input().split()))

    if min(data)!= 1:
        print(1)


    blank =[]

    for i in range(1,n+1):
        result = list(combinations(data,i ))
        for e in result:
            temp = sum(e)
            if temp not in blank:

                blank.append(temp)

    blank.sort()

    answer = 0

    for i in range(len(blank)):
        if blank[i] != i+1:
            print(blank[i-1] +1)
            break



main()