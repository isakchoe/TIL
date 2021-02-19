



def cal():

    n  = int(input())

    num = list(map(int, input().split()))

    plus, mi, mult, div = map(int, input().split())

    result = num[0]


    for i in range(1,len(num)):
        if result == 1 or num[i] == 1:
            if plus != 0:
                result += num[i]
                plus = plus - 1

            elif plus == 0 and mult != 0:
                result = result * num[i]
                mult = mult -1

            elif plus == 0 and mult == 0:

                if div !=0:
                    result = result//num[i]
                    div = div -1
                else:
                    result = result - num[i]
                    mi = mi -1


        else:
            if mult != 0:
                result = result * num[i]
                mult = mult -1

            elif mult == 0 and plus !=0 :
                result = result + num[i]
                plus = plus -1

            elif mult == 0 and plus == 0 :
                if result > num[i]:

                    if mi != 0:
                        result = result - num[i]
                        mi = mi -1

                    else:
                        result = result // num[i]
                        div = div - 1


                else:

                    if div != 0:
                        result = result // num[i]
                        div = div -1
                    else:
                        result = result - num[i]
                        mi = mi -1



    return result



print(cal())

