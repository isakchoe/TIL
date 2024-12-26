# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        self.pre_order(root, 0, arr)
        return arr

    def pre_order(self, node, depth, arr):
        if node is None:
            return

        if len(arr) -1 < depth:
            arr.append(node.val)
        else:
            if arr[depth] < node.val:
                arr[depth] = node.val

        self.pre_order(node.left, depth+1, arr)
        self.pre_order(node.right, depth +1, arr)


