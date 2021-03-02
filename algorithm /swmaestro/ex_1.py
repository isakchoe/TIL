

def main():
    s_list = list(input().split())
    n = int(input())


    pro = []
    back = []

    for i in range(n):

        a, b = input().split()

        pro.append(a)
        back.append(b)

    solo_skill = ''

    for i in range(len(pro)):
        if pro[i] not in back:
            solo_skill = pro[i]



    re= []
    for i in range(n):
        if pro[i] == solo_skill:
            re.append(back[i])

    for i in range(n):
        if pro[i] in re :
            temp = pro[i] + " " + back[i]





