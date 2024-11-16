

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # help from chatgpt
    # dfs 이용!!
    # 전위 순회, 중위 순회의 특징을 잘 이해해야함
    # 결국... 왼쪽 서브 트리 먼저 순회하기에... 구성요소는 같다는것!.
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # The first element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the root in inorder
        index = inorder.index(root_val)

        # Elements to the left of 'index' in inorder are the left subtree
        # Elements to the right of 'index' in inorder are the right subtree
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])

        return root
