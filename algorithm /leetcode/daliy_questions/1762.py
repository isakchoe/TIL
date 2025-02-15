
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        all_tuple = {}

        answer = 0

        for i in range(len(nums)):
            for j in range( i +1, len(nums)):
                temp = nums[i] * nums[j]

                if temp not in all_tuple:
                    all_tuple[temp] = 1
                else:
                    all_tuple[temp] += 1


        for k, count in all_tuple.items():

            if count > 1:
                combis = (count) * (count -1) // 2
                all_permutations = combis * 8
                answer += all_permutations

        return answer
