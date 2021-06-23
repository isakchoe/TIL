
def solution(nums):
    #     딕셔너리 이용
    #       종류 개수 파악

    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1

    #     종류 개수
    n = len(dic)
    # 선택 개수
    m = len(nums)//2

    if n >= m:
        return m
    else:
        return n