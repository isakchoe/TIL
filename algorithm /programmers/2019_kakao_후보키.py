from itertools import combinations


def solution(relation):
    #
    #     1,2,3 개 늘려가면서 --> 최소성 만족하면 제거

    #     칼럼 개수
    n = len(relation[0])

    answer = 0

    dic = {}
    for i in range(n):
        dic.setdefault(i, 0)

    #     1개
    for i in range(1, n + 1):

        #         dic에서 0인 것만 리스트에 추가
        blank = []
        for key in dic:
            if dic[key] == 0:
                blank.append(key)

        if len(blank) == 0:
            break

        #         조합
        temp = list(combinations(blank, i))
        print(temp)



        #         탐색
        for j in range(len(temp)):
            pivot_cols = sorted(temp[j])
            break_point = 0
            check_dic = {}
            for r in relation:

                char = ""
                for index in pivot_cols:
                    char += r[index]

                #                 check
                if char not in check_dic:
                    check_dic[char] = 1
                else:
                    break_point += 1
                    break
            #            해당 컬럼으로 유일성 확인 가능!
            if break_point == 0:
                for t in pivot_cols:
                    dic[t] = 1
                print(pivot_cols)
                answer += 1


    return answer

relation = [['a',"1",'aaa','c','ng'],['b',"1",'bbb','c','g'],['c',"1",'aaa','d','ng'],['d',"2",'bbb','d','ng']]




if __name__ == '__main__':
    print(solution(relation))
    # print(list(combinations([1,2,3,4], 5)))