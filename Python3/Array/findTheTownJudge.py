# https://leetcode.com/problems/find-the-town-judge/

from typing import List

class Solution:
    # Graph representation of solution, used this one first
    # Time: O(v + e) - where v is number of vertices and e is number of edges
    # Space: O(v + e) - for adjacency list
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people = [i for i in range(1, N + 1)]
        adj = {}
        for pair in trust:
            if pair[0] in adj:
                adj[pair[0]].add(pair[1])
            else:
                adj[pair[0]] = {pair[1]}
        potential_judge = None
        for person in people:
            if person not in adj:
                if potential_judge is None:
                    potential_judge = person
                else:
                    return -1
        if potential_judge is None:
            return -1
        for v in adj:
            if potential_judge not in adj[v]:
                return -1
        return potential_judge

class Solution2:
    # Time: O(v + e)
    # Space: O(e)
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

if __name__ == '__main__':
    obj = Solution2()
    # assert(obj.findJudge(2, [[1,2]]) == 2)
    # assert(obj.findJudge(3, [[1,3],[2,3]]) == 3)
    # assert(obj.findJudge(3, [[1,3],[2,3],[3,1]]) == -1)
    # assert(obj.findJudge(3, [[1,2],[2,3]]) == -1)
    print(obj.findJudge(3, [[1,2],[1,3]]))
    # assert(obj.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3)

