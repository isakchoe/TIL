

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        answer = []

        if root == None:
            return answer

        q = deque()

        q.append([0, root])

        temp = []
        now_level = 0

        while q:
            level, node = q.popleft()

            if node == None:
                continue

            # 자식 노드 큐 삽입
            q.append([level + 1, node.left])
            q.append([level + 1, node.right])

            if level == now_level:
                temp.append(node.val)
            else:
                answer.append(temp)
                temp = [node.val]
                now_level += 1

        answer.append(temp)
        return answer




