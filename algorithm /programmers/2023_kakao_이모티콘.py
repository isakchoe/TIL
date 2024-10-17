

import itertools

def solution(users, emoticons):

    discounts = [0.9, 0.8, 0.7, 0.6]  # 10%, 20%, 30%, 40%에 해당하는 할인율

    saled_list = apply_discounts(emoticons, discounts)


    answer_include = 0
    answer_income = 0


    for idx, sale_price in enumerate(saled_list):
        temp_include, temp_income = get_income_include(sale_price, users)

        # 순서쌍으로 저장해야함.
        if temp_include > answer_include:
            answer_include = temp_include
            answer_income = temp_income

        elif temp_include == answer_include:
            if temp_income > answer_income:
                answer_income = temp_income

    return [answer_include, answer_income]


# 각 가격에 대한 세일 적용된 가격을 구하는 함수
def apply_discounts(prices, discounts):

    discounted_prices = [[(discount, price * discount) for discount in discounts] for price in prices]

    # 가능한 모든 경우의 수 구하기
    all_combinations = list(itertools.product(*discounted_prices))
    return all_combinations

def get_income_include(price_list, users):

    total_income = 0
    total_include = 0

    for want, limit in users:
        to_buy = 0

        # 구매
        for sale_rate, saled_price in price_list:
            if 100 - sale_rate*100 >= want :
                to_buy += saled_price

        if to_buy >= limit:
            total_include += 1
        else:
            total_income += to_buy

    return [total_include, int(total_income)]







users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))

