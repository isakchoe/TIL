

class Solution:

    def dfs(self, rooms, start_room, visited):
        visited[start_room] = True

        for key in rooms[start_room]:
            if visited[key] == False:
                self.dfs(rooms, key, visited)


    def canVisitAllRooms(self, rooms: [int]) -> bool:
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)

        for i in range(n):
            if visited[i] == False:
                return False
        return True

a = Solution()

rooms = [[1],[2],[3],[]]
print(a.canVisitAllRooms(rooms))