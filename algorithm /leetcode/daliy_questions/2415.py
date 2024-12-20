
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()

        q.append(root)

        node_list = []

        while q:
            node = q.popleft()

            if node is None:
                continue

            node_list.append(node.val)

            q.append(node.left)
            q.append(node.right)


        idx = 0
        n = 1

        result_list = []

        while idx < len(node_list):
            # 홀수 or 짝수 레벨만 접근하는 유형 자주 나옴.
            if  2**n -1 <=idx <2**(n+1)-1:
                for j in range(2**(n+1)-2, 2**n-2, -1):
                    result_list.append(TreeNode(node_list[j]))
                idx = 2**(n+1) -1
                n += 2
            else:
                result_list.append(TreeNode(node_list[idx]))
                idx += 1

        result_list = self.connect_node(result_list)
        return result_list[0]


    def connect_node(self, node_list):
        for i in range(len(node_list)):
            now = node_list[i]

            # 정이진트리 특성..
            if i*2 +1 < len(node_list):
                now.left = node_list[i*2 +1]
                now.right = node_list[i*2 +2]
        return node_list

