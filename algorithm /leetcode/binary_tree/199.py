
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> [int]:

        if root is None:
            return []

        answer = []
        depth_set = set()

        self.dfs(root, 0, answer, depth_set)
        return answer


    def dfs(self, node, depth, answer, depth_set):
        if node is None:
            return

        if depth not in depth_set:
            depth_set.add(depth)
            answer.append(node.val)

        # right
        self.dfs(node.right, depth+1, answer, depth_set)

        # left
        self.dfs(node.left, depth+1, answer, depth_set)