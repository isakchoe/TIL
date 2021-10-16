

def solution(triangle):

    # triangle 탐색하면서 자기 인덱스, 자기인덱스-1 탐색,  최대값 갱신 max() 로

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 시작
            if j == 0 :
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            # 마지막
            elif j == len(triangle[i]) -1 :
                triangle[i][j] += triangle[i-1][j-1]
            # 중간
            else:
                triangle[i][j] = max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])


    answer = max(triangle[-1])

    return answer




