
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []

        if len(nums) == 0:
            return answer
        temp = str(nums[0])
        end = ""

        for i in range(1 ,len(nums)):
            if nums[i] - nums[ i -1] != 1:
                if end == "":
                    answer.append(temp)
                else:
                    answer.append(temp + "->" + end)
                temp = str(nums[i])
                end = ""
            else:
                end = str(nums[i])

        if end == "":
            answer.append(temp)
        else:
            answer.append(temp + "->" + end)


        return answer