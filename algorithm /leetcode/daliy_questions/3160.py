
class Solution:
    def queryResults(self, limit: int, queries: [[int]]) -> [int]:
        node_dic = {}
        color_dic = {}

        answer = 0
        answer_list = []
        for n, c in queries:
            # 컬러 update
            if n in node_dic:
                # 이전 컬러 감소
                pre_c = node_dic[n]
                color_dic[pre_c] -= 1

                if color_dic[pre_c] == 0:
                    answer -= 1

            #  새로운 컬러
            if c not in color_dic or color_dic[c] == 0:
                color_dic[c] = 1
                answer += 1
            else:
                color_dic[c] += 1
            node_dic[n] = c

            answer_list.append(answer)
        return answer_list

a = Solution()
limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(a.queryResults(limit,queries))

