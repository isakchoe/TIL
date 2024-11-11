

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start = 0
        end = 0

        total_length = set()
        answer = 1


        # 종료조건이 두개인 경우 유의하기..
        # temp_answer 갱신..
        while start < len(s):
            # new
            if s[end] not in total_length:
                total_length.add(s[end])
                # 종료 조건
                if end == len(s) -1:
                    answer = max(answer, len(total_length))
                    break
                end += 1
            # 중복
            else:
                answer = max(answer, len(total_length))

                # 종료 조건
                if end == len(s)-1:
                    break

                total_length.remove(s[start])
                start += 1

        return answer

a = Solution()
s = "au"
print(a.lengthOfLongestSubstring(s))




