

def solution(w,h):
    # 정사각형
    if w == h:
        return (h-1)*w
    # 직사각형
    # 기울기 이용!!
    #  기울기이용해서 높이 구하고, 그에 맞게 개수 세기
    # 직각삼각형 2개니깐, 곱하기 2
    else:
        answer = 0
        for i in range(w):
            temp = (h * i)//w
            answer += temp

        return 2*answer

