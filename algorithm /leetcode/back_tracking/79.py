

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visited = [[False]*n for _ in range(m)]

        dic = {}

        for s in word:
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(word, [board[i][j]], i, j, visited, board):
                        return True
                    visited[i][j] = False
        return False


    def dfs(self, word, temp_arr, row, col, visited, board):
        m = len(board)
        n = len(board[0])

        #  재방문...
        # 방문 처리는 밖에서 할 것인가? 안에서 할것인가...
        if visited[row][col]:
            return
        visited[row][col] = True


        # 꼭 길이가 다 맞아야 확인해야해??
        if len(temp_arr) == len(word):
            result = ''.join(temp_arr)
            if result == word :
                return True
            return False

        # backtracking 2
        temp_result = ''.join(temp_arr)
        if temp_result != word[:len(temp_arr)]:
            return False


        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]

            if 0<= nr < m and 0<= nc < n:
                next_string = board[nr][nc]

                if next_string == word[len(temp_arr)]:
                    if not visited[nr][nc]:  # 최대한, depth 를 줄이기 위해서는 밖에서 방문 여부 파악하는 것이 좋음...
                        # 추가
                        temp_arr.append(next_string)
                        result = self.dfs(word, temp_arr, nr, nc, visited, board)

                        if result:
                            return True
                        # back = 재방문했을때는,, 방문표시를 풀어주면 안된다!
                        visited[nr][nc] = False
                        temp_arr.pop()
        return False


a = Solution()
board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
word = "AAAAAAAAAAAAABB"
print(a.exist(board, word))
