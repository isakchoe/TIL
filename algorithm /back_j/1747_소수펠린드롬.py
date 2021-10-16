import math


# 펠린드롬 판별
def is_pal(string):

    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True

# 소수판별
def is_prime(number):

    if number == 1:
        return False

    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False

    return True



# 입력
n = int(input())


while True:
    # 펠린드롬 판별
    if is_pal(str(n)):
        if is_prime(n):
            print(n)
            break

    n += 1


