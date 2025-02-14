
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def __init__(self):
        self.total = 0


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node == None:
                continue

            # root 인 새로운 시작
            self.dfs(node, node.val, targetSum)

            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

        return self.total


    def dfs(self, node, temp_sum, k ):

        if temp_sum == k:
            self.total += 1

        if node.right != None:
            self.dfs(node.right, temp_sum + node.right.val , k)

        if node.left != None:
            self.dfs(node.left, temp_sum + node.left.val , k)

