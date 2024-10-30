

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        arr = []
        self.dfs(root, arr)
        return arr[k-1]


    # 중위 순회?? - 항상 기준은 == 루트(본인)노드
    # bst 는 - 왼쪽--> 중간 ---> 오른쪽
    # 중위순휘, 전위, 후위 -> 모든 서브트리 순서는: left -> right
    def dfs(self, node, arr):
        # left
        if node.left != None:
            self.dfs(node.left, arr)

        arr.append(node.val)

        # right
        if node.right != None:
            self.dfs(node.right, arr)
