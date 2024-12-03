
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return  s

        is_down = True
        row = 0
        count = 0
        n = len(s)

        dic = {key:"" for key in range(numRows)}

        while count < n:
            dic[row] += s[count]

            # 위 도달
            if row == 0:
                is_down = True
            # 끝 도달
            if row == numRows -1:
                is_down = False

            if is_down:
                row += 1
            else:
                row -= 1
            count += 1

        answer = ""
        for i in range(numRows):
            answer += dic[i]
        return answer

a = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(a.convert(s, numRows))




