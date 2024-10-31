

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:

        arr = []
        self.dfs(root, arr)

        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True


    def dfs(self, node, arr):

        if node.left != None:
            self.dfs(node.left, arr)

        arr.append(node.val)

        if node.right != None:
            self.dfs(node.right, arr)

