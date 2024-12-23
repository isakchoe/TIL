

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: [TreeNode]) -> int:
        level_dic = {}
        flag_dic = {}

        self.dfs(root, 0, level_dic, flag_dic)

        answer = 0

        for k in flag_dic.keys():
            # 정렬되지 않은 녀석만 정렬 시도.
            arr = level_dic[k]
            count = self.min_swaps_to_sort(arr)
            answer += count

        return answer

    def dfs(self, node, level, level_dic, flag_dic):
        if node is None:
            return

        if level not in level_dic:
            level_dic[level] = [node.val]
        else:
            if node.val < level_dic[level][-1]:
                flag_dic[level] = True
            level_dic[level].append(node.val)

        self.dfs(node.left, level+1, level_dic, flag_dic)
        self.dfs(node.right, level+1, level_dic, flag_dic)

    # helped from gpt
    def min_swaps_to_sort(self, arr):
        n = len(arr)
        swaps = 0

        # 배열의 값과 원래 인덱스를 저장
        indexed_arr = [(value, index) for index, value in enumerate(arr)]
        # 값을 기준으로 정렬
        indexed_arr.sort()

        # 방문 여부 확인용 배열
        visited = [False] * n

        for i in range(n):
            # 이미 방문했거나 정렬된 위치라면 건너뜀
            if visited[i] or indexed_arr[i][1] == i:
                continue

            # 사이클의 크기 계산
            cycle_size = 0
            x = i

            while not visited[x]:
                visited[x] = True
                x = indexed_arr[x][1]
                cycle_size += 1

            # 사이클 크기가 2 이상이면 (cycle_size - 1)만큼 교환 필요
            if cycle_size > 1:
                swaps += cycle_size - 1
        return swaps


a = Solution()

arr = [1,2,3,4]
print(a.sort_change(arr))