

# helped from gpt
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        arr = [0] * (2 * n - 1)
        size = len(arr)

        visited = [False] * (n + 1)

        def dfs(idx):
            # idx 조절..
            while idx < size and arr[idx] != 0:
                idx += 1

            # end  - dfs 는 종료조건 존재해야함..
            if idx == size:
                return True

            for num in range(n, 0, -1):
                if visited[num]:
                    continue

                #  1 아닌 경우
                if num != 1:
                    if arr[idx] == 0 and num + idx < size and arr[idx + num] == 0:
                        arr[idx] = arr[idx + num] = num
                        visited[num] = True

                        # 이게 핵심!!
                        if dfs(idx + 1):
                            # 종료조건이 있다면, 이것을 받아줘야 함 -> 그리고 해당지점을 기반으로, 백트래킹..
                            return True
                            # back
                        arr[idx] = arr[idx + num] = 0
                        visited[num] = False

                else:
                    arr[idx] = 1
                    visited[num] = True

                    if dfs(idx + 1):
                        return True

                    arr[idx] = 0
                    visited[num] = False

                    # 여기도 핵심..
            # num 을 모두 방문하지 못하고, 끝나는 경우...
            return False

        dfs(0)
        return arr




