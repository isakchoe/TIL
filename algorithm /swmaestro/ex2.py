


def main():
    p, n, h = map(int, input().split())

    answer = []

    for i in range(n):
        x, y = map(int, input().split())

        answer.append([x,y])




    answer.sort(key = lambda  x: x[0])

    pc =[]
    total = []
    for i in range(len(answer)):
        if answer[i][0] not in pc:
            pc.append(answer[i][0])
            if answer[i][1] <=h:

                total.append(answer[i][1])
            else:
                total.append(0)

        else:
            if answer[i][1] <= h:
                if total[-1] + answer[i][1] <=h:

                    total[-1] += answer[i][1]




    for i in range(len(total)):
        if total[i] >h :
            total[i] = 1000 * h
        else:
            total[i] = 1000 * total[i]

    for i in range(len(total)):
        print(pc[i], total[i])




main()
