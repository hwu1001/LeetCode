# https://leetcode.com/problems/check-if-it-is-a-straight-line/

from typing import List

class Solution:
    # Time: O(n)
    # Space: O(1)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def getSlope(pt1: List[int], pt2: List[int]) -> int:
            if pt2[0] - pt1[0] == 0:
                return None
            return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
        if len(coordinates) < 2:
            return False
        if len(coordinates) == 2:
            return True
        slope = getSlope(coordinates[0], coordinates[1])
        prev_coord = coordinates[1]
        for coord in coordinates[2:]:
            if getSlope(prev_coord, coord) != slope:
                return False
            prev_coord = coord
        return True

class Solution2:
    # Checking slope with multiplication instead to avoid divide by zero
    # Slope for three points: (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)
    # => (x1 - x0) * (y - y1) = (x - x1) * (y1 - y0)
    # Time: O(n)
    # Space: O(1)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True



if __name__ == '__main__':
    obj = Solution2()
    assert(obj.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True)
    assert(obj.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False)
    assert(obj.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]) == False)