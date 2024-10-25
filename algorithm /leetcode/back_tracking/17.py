

class Solution:
    def letterCombinations(self, digits: str) -> [str]:

        if len(digits) == 0:
            return []

        answer = set()
        self.dfs_go("", 0, len(digits), digits, answer)

        return list(answer)

    def dfs_go(self, temp_string, depth, ojt_depth, digits, answer):

        num_string = [0, [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                      ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        if depth == ojt_depth:
            answer.add(temp_string)
            return temp_string

        string_list = num_string[int(digits[depth])]

        before = temp_string
        for string in string_list:
            temp_string += string
            self.dfs_go(temp_string, depth + 1, ojt_depth,digits, answer)

            # back
            temp_string = before




a = Solution()
digits = "23"
print(a.letterCombinations(digits))