
import heapq

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:

        ad_list = [[] for _ in range(numCourses)]
        ad_dic = {k: 0 for k in range(numCourses)}

        for  a, b in prerequisites:
            ad_list[b].append(a)
            ad_dic[a] += 1

        q = []
        heapq.heapify(q)

        for k, v in ad_dic.items():
            if v == 0:
                heapq.heappush(q, [0, k])

        answer = []
        while q:
            pre_req, course_num = heapq.heappop(q)

            answer.append(course_num)

            #  수강 -> 다음 과목 차수 하나씩 감소.
            for next_course in ad_list[course_num]:
                ad_dic[next_course] -= 1

                if ad_dic[next_course] == 0:
                    # 0인 차수만 q 에 넣는다.
                    heapq.heappush(q, [0, next_course])

        # 싸이클 여부 파악, flag 로도 가능
        if len(answer) != numCourses:
            return []
        return answer


a = Solution()
numCourses = 3
prerequisites = [[1 ,0] ,[1 ,2] ,[0 ,1]]

print(a.findOrder(numCourses, prerequisites))
