# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:

        q = deque()

        q.append([root.right, 1])
        q.append([root.left, 1])

        now_depth = 1
        temp_sum = 0
        temp_count = 0

        answer = [root.val]

        while q:
            now, depth = q.popleft()

            if now == None:
                continue

            print(now.val)
            if depth != now_depth:
                answer.append(temp_sum / temp_count)
                temp_sum = now.val
                temp_count = 1
                now_depth = depth

            else:
                temp_sum += now.val
                temp_count += 1

            q.append([now.left, depth + 1])
            q.append([now.right, depth + 1])

        if temp_count != 0:
            answer.append(temp_sum / temp_count)

        return answer
