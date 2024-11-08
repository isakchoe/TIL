

from collections import deque
import copy

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()

        q.append([0,root])

        answer = []
        now_level = 0
        is_left = True

        temp = []
        while q:
            level, node = q.popleft()

            # none 일 경우, 로직 고려하기..
            if node is None:
                continue

            if level == now_level:
                temp.append(node.val)

            # 계층 변화
            else:
                copy_temp = copy.deepcopy(temp)

                if is_left:
                    answer.append(copy_temp)
                    is_left = False
                else:
                    copy_temp.reverse()
                    answer.append(copy_temp)
                    is_left = True

                temp = [node.val]
                now_level = level

            # 큐 삽입
            q.append([level+1, node.left])
            q.append([level+1, node.right])


        #  edge 케이스 항상... 고려하기... 이런 포인트가 시간 잡아 먹음..
        if len(temp) != 0:
            if is_left:
                answer.append(temp)
            else:
                temp.reverse()
                answer.append(temp)

        return answer