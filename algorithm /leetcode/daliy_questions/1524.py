
class Solution:
    # gpt
    def numOfSubarrays(self, arr: [int]) -> int:
        mod = 10**9 + 7
        even_count = 1  # count of even prefix sums (prefix sum = 0 initially)
        odd_count = 0   # count of odd prefix sums
        prefix = 0      # current prefix sum
        result = 0      # result for subarrays with odd sum

        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                # If prefix sum is even, an odd subarray ending here
                # can only come from a previous odd prefix.
                result = (result + odd_count) % mod
                even_count += 1
            else:
                # If prefix sum is odd, a subarray ending here is odd
                # if its starting prefix was even.
                result = (result + even_count) % mod
                odd_count += 1

        return result


#my answer
class Solution:
    def numOfSubarrays(self, arr: [int]) -> int:
        acc_sum = [arr[0]]

        for i in range(1, len(arr)):
            temp = arr[i] + acc_sum[-1]
            acc_sum.append(temp)

        answer = 0
        odd = 0
        even = 0

        for i in range(len(acc_sum)):
            if acc_sum[i] %2 ==0:
                even += 1
            else:
                odd += 1
        answer += odd

        for i in range(len(acc_sum)):
            # pop 이 홀수이고
            if acc_sum[i] % 2==1:
                # 현재가 짝수일때, -> 홀수로 변함
                answer += even
                odd -= 1
            else:
                # 짝수일때는, 변화 x , 그대로 홀수인게 홀수
                answer += odd
                even -= 1

        mod = 10**9 + 7
        return answer % mod


a = Solution()
arr = [1,3,5]
print(a.numOfSubarrays(arr))



