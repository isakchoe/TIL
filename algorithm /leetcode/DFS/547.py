

class Solution:

    def find_parent(self, number, parent):
        if parent[number] == number:
            return number
        parent[number] = self.find_parent(parent[number], parent)
        return parent[number]

    def union(self, a, b, parent):
        parent_a = self.find_parent(a, parent)
        parent_b = self.find_parent(b, parent)

        if parent_a > parent_b:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a


    def findCircleNum(self, isConnected: [int]) -> int:

        n = len(isConnected)
        parent = [ x for x in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    if isConnected[i][j] == 1:
                        self.union(i, j, parent)


        for i in range(n):
            self.find_parent(i, parent)


        answer = len(set(parent))
        return answer



a = Solution()
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(a.findCircleNum(isConnected))

