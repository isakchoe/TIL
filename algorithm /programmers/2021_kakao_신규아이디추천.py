

def solution(new_id):
    # 아이디 규칙
    #  3자이상 15자 이하
    #  마침표. 처음, 끝 X 연솓 x
#     주어진 조건에 맞게 구현 끝!


    #  1단계 대문자--> 소문자
    new_id = new_id.lower()

    possible = ['-', '_', '.',]

    # 2단계
    new_list = []
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in possible:
            new_list.append(char)


    # 3단계
    new_list_3 = []
    count = 0
    for i in range(len(new_list)):
        if new_list[i] == '.':
            count += 1
            # 마지막도 '.' 일경우 넣어줘야한다.
            if i == len(new_list)-1:
                new_list_3.append('.')
        else:
            if count == 0:
                new_list_3.append(new_list[i])
            else:
                new_list_3.append('.')
                new_list_3.append(new_list[i])
                count = 0

    # 4단계
    # 인덱스 에러 처리해줘야 한다. (빈문자열일경우!)
    if len(new_list_3)!=0 and new_list_3[0] == '.':
        new_list_3.pop(0)

    if len(new_list_3) !=0 and new_list_3[-1] == '.':
        new_list_3.pop()

    # 5단계
    if len(new_list_3) == 0 :
        new_list_3.append('a')

    # 6단계
    while len(new_list_3) > 15:
        new_list_3.pop()

    # 마침표 확인
    if new_list_3[-1] == '.':
        new_list_3.pop()


    # 7 단계
    while len(new_list_3) <=2:
        temp = new_list_3[-1]
        new_list_3.append(temp)

    return ''.join(new_list_3)
