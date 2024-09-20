

from collections import  deque

class Solution:
    def get_destination(self, board):
        n = len(board)
        ad_list = [0] * (n * n + 1)
        curr = 1

        for i in range(n-1, -1, -1):
            for j in range(n):
                if n % 2 == 0:
                    # 정순
                    if i % 2 == 1:
                        ad_list[curr] = board[i][j]
                    else:
                        ad_list[curr] = board[i][-(j+1)]
                else:
                    # 정순
                    if i%2 == 0:
                        ad_list[curr] = board[i][j]
                    else:
                        ad_list[curr] = board[i][-(j + 1)]

                curr += 1
        return ad_list

    def snakesAndLadders(self, board: [int]) -> int:
        q = deque()
        n = len(board)

        ad_list = self.get_destination(board)

        q.append(1)

        visited = set()

        count = 0
        while q:

            for _ in range(len(q)):
                curr = q.popleft()

                # 도달
                if curr == n*n:
                    return count

                # 재방문
                if curr in visited:
                    continue
                # 방문 처리
                visited.add(curr)

                for next in range(curr+1, min(curr +6, n*n)+1):

                    if ad_list[next] == -1:
                        q.append(next)
                    else:
                        q.append(ad_list[next])

            count += 1

        return -1












# import collections
#
# class Solution:
#   def snakesAndLadders(self, board: list[list[int]]) -> int:
#     n = len(board)
#     ans = 0
#     q = collections.deque([1])
#     seen = set()
#     A = [0] * (1 + n * n)  # 2D -> 1D
#
#     for i in range(n):
#       for j in range(n):
#         A[(n - 1 - i) * n + (n - j if (n - i) % 2 == 0 else j + 1)] = board[i][j]
#
#     print(A)
#
#     while q:
#       ans += 1
#       for _ in range(len(q)):
#         curr = q.popleft()
#         print(curr)
#         for next in range(curr + 1, min(curr + 6, n * n) + 1):
#           dest = A[next] if A[next] > 0 else next
#           if dest == n * n:
#             print("-----------")
#             print(curr, dest)
#             return ans
#           if dest in seen:
#             continue
#           q.append(dest)
#           seen.add(dest)
#
#     return -1



# board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# board = [[-1,4,-1],[6,2,6],[-1,3,-1]]
# board = [[-1,15,9,1,-1],[-1,-1,10,5,19],[18,-1,23,9,-1],[1,13,-1,16,20],[-1,10,10,25,13]]
# board = [[-1,1,2,-1],
#          [2,13,15,-1],
#          [-1,10,-1,-1],
#          [-1,6,2,8]]
# #
# board = [[1,1,-1],
#          [1,1,1],
#          [-1,1,1]]

board = [[-1,-1,-1,-1,48,5,-1],
         [12,29,13,9,-1,2,32],
         [-1,-1,21,7,-1,12,49],
         [42,37,21,40,-1,22,12],
         [42,-1,2,-1,-1,-1,6],
         [39,-1,35,-1,-1,39,-1],
         [-1,36,-1,-1,-1,-1,5]]

# board = [[-1,-1,27,13,-1,25,-1],
#          [-1,-1,-1,-1,-1,-1,-1],
#          [44,-1,8,-1,-1,2,-1],
#          [-1,30,-1,-1,-1,-1,-1],
#          [3,-1,20,-1,46,6,-1],
#          [-1,-1,-1,-1,-1,-1,29],
#          [-1,29,21,33,-1,-1,-1]]

a = Solution()

print(a.snakesAndLadders(board))
# print(a.get_row_col(29, 7))


