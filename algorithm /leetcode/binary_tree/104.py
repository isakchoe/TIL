
class Solution:
    def maxDepth(self, root) -> int:
        def Dfs(node, depth):
            if node == None:
                return depth - 1

            a = Dfs(node.left, depth + 1)
            b = Dfs(node.right, depth + 1)
            return max(a ,b)
        answer = Dfs(root, depth=1)
        return answer




# global 사용시 주의할 것. 함수 밖으로..
#  테스트 케이스 여러개일경우, global 은 초기화 안되는 문제....

