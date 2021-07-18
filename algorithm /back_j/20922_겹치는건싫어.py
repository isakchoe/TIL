

# 카카오 블라인드, 보석쇼핑이랑 비슷

# 딕셔너리 이용, 투포인터
# 조건 만족할때까지 최대한 길이 늘리기
#  조건 벗어나면, 길이 줄이기


# 입력받기
n, k = map(int,input().split())
arr = list(map(int, input().split()))

# 딕셔너리
dic = {}

# 투포인터
start = 0
end = 0

# 정답
answer = 0

# end를 끝까지 탐색
while end < len(arr):
    # dic에 없는 경우
    if arr[end] not in dic:
        dic[arr[end]] = 1

        # 정답 길이 저장
        temp = end - start +1
        if temp > answer:
            answer = temp

        # end 가 끝이 아니면  증가
        if end != len(arr) :
            end += 1

    # 이미 해당 숫자 나온 경우
    else:
        # k 초과하지 않는 경우
        if dic[arr[end]] < k:
            dic[arr[end]] += 1

            # 정답 갱신
            temp = end - start + 1
            if temp > answer:
                answer = temp
            # end 길이 확인
            if end != len(arr) :
                end += 1
            continue

        # k 개수 초과하는 경우
        elif dic[arr[end]] >= k:

            # start 증가 ==> 길이 감소
            dic[arr[start]] -= 1
            if dic[arr[start]] == 0:
                del(dic[arr[start]])

            start += 1

print(answer)












