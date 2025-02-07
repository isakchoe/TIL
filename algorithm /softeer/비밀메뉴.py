
import sys

M, N, K = map(int, input().split())

s_arr = list(map(int, input().split()))

input_arr = list(map(int, input().split()))


s_len = len(s_arr)

answer = "normal"
for i in range(len(input_arr)):
    temp = input_arr[i:i+s_len]

    if str(temp) == str(s_arr):
        answer = "secret"
        break

print(answer)