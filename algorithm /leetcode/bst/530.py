
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: [TreeNode]) -> int:
        arr = []
        self.dfs(root, arr)

        min_diff = 100000
        for i in range(1,len(arr)):
            diff = abs(arr[i] - arr[i-1])
            min_diff = min(min_diff, diff)
        return min_diff

    def dfs(self, node, arr):

        # left
        if node.left != None:
            self.dfs(node.left, arr)

        arr.append(node.val)
        # right
        if node.right != None:
            self.dfs(node.right, arr)
