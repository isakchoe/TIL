import copy


class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:

        min_count = target // min(candidates)

        if min_count == 0:
            return []

        candidates.sort()
        answer = set()
        self.dfs(0, min_count, [], 0, target, answer, candidates)

        list_answer = []
        for e in answer:
            list_answer.append(list(e))

        return list_answer

    def dfs(self, now_depth, depth, now_combi, now_sum, target, answer, candidates):
        # 종료 조건 1: depth 초과
        if now_depth > depth:
            return

        # 종료조건 2: target 일치
        if now_sum == target:
            temp_list = copy.deepcopy(now_combi)
            temp_list.sort()
            temp = tuple(temp_list)
            answer.add(temp)
            return

        # 종료조건 3: 지금까지 합이 target 보다 큰 경우. -> 더 진행할 필요가 없다.
        elif now_sum > target:
            return

        for candidate in candidates:
            #  정렬되어 있기에 더 진행할 필요 없다.
            if now_sum + candidate > target:
                break

            # 더하기
            now_sum += candidate
            now_combi.append(candidate)
            self.dfs(now_depth +1, depth, now_combi, now_sum, target, answer, candidates)

            # back
            now_sum -= candidate
            now_combi.pop()



a = Solution()
candidates = [5,10,8,4,3,12,9]
target = 27
print(a.combinationSum(candidates, target))


