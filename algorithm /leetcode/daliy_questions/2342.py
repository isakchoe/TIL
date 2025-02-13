class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            digit_key = self.get_d_key(num)

            if digit_key not in dic:
                dic[digit_key] = [num]
            else:
                dic[digit_key].append(num)

        answer = -1

        for v_list in dic.values():

            if len(v_list) < 2:
                continue

            v_list.sort()

            temp_sum = v_list[-1] + v_list[-2]
            answer = max(answer, temp_sum)

        return answer

    def get_d_key(self, num):
        str_num = list(str(num))

        total = 0

        for s in str_num:
            total += int(s)
        return total 


