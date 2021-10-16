def main():

    n = input()
    length = len(n)


    half = length//2

    r_total = 0
    l_total = 0

    for i in range(half):
        l_total += int(n[i])

    for e in range(half, length):
        r_total += int(n[e])

    if r_total == l_total :
        print("LUCKY")
    else:
        print("READY")



main()

