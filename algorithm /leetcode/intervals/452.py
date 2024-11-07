

class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        points.sort()
        over_end = points[0][1]

        answer = 1

        for i in range(1, len(points)):
            temp_s, temp_e = points[i][0], points[i][1]

            # 겹치지 않으면, 패스
            if temp_s > over_end:
                answer += 1
                over_end = temp_e
                continue

            # 겹치는 경우 고려
            # 완전히 포개지는 경우
            if over_end >= temp_e:
                over_end = temp_e

        return answer


a = Solution()
points = [[1,2],[3,4],[5,6],[7,8]]
print(a.findMinArrowShots(points))