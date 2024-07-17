
class Solution:

    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:

        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        start_point = 0
        current_gas = 0
        total_gas = 0

        for i in range(len(diff)):
            current_gas += diff[i]
            total_gas += diff[i]

            if current_gas < 0 :
                start_point = i +1
                current_gas = 0


        if total_gas < 0:
            return -1
        return start_point



s = Solution()

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

print(s.canCompleteCircuit(gas, cost))