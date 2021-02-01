def main():
    n = input()
    int_total = 0
    a_list = []
    for i in range(len(n)):
        if n[i].isdigit() :
            int_total += int(n[i])
        else:
            a_list.append(n[i])



    a_list.sort()

    new_char = ''.join(a_list)




    print(new_char + str(int_total))


main()