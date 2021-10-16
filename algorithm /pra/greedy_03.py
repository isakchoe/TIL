

def main():


    n = input()

    answer = 0
    start = n[0]

    for i in range(len(n)):
        if n[i] != start:
            answer +=1
            start = n[i]

    print(round(answer/2))





main()
