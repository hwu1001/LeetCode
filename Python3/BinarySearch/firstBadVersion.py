# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# test version
versions = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        11: False,
        12: False,
        13: False,
        14: False,
        15: False,
        16: False,
        17: False,
        18: False,
        19: False,
        20: False,
        21: False,
        22: False,
        23: False,
        24: False,
        25: False,
        26: False,
        27: False,
        28: True
    }

# versions = [False] * 100000
# versions[75000:] = [True] * len(versions[75000:])

# versions = [False] * 900000
# versions[255000:] = [True] * len(versions[255000:])

def isBadVersion(version):
    return versions[version]


class Solution(object):
    # Time: O(log(n))
    # Space: O(1)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # For testing with arrays set left to 0 and right to n - 1
        left, right = 1, n
        while left <= right:
            # Since integer operations in Python cannot overflow
            # we don't have to do it this way, but doing it this way for consistency.
            # In many other languages just doing (left + right) // 2 can lead to overflow bugs
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    # This was my first attempt at the problem (and it worked, but doesn't look as nice
    # as the above solution)
    # Time: O(log(n))
    # Space: O(1)
    def firstBadVersionFirstTry(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1 # For testing with arrays set this to 0
        last = n # For testing with arrays set this to n - 1
        mid = 0
        statusChange = 0
        isBad = None
        lastGood = 0
        lastBad = 0
        # Use first loop to find the first bad version
        while first <= last and statusChange < 3:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid - 1
                if isBad is None or not isBad:
                    statusChange += 1
                isBad = True
                lastBad = mid
            else:
                first = mid + 1
                if isBad is None or isBad:
                    statusChange += 1
                isBad = False
                lastGood = mid
            if abs(lastBad - lastGood) > 50:
                statusChange -= 1

        change = 0
        if isBad:
            change = -1
        else:
            change = 1
        while(True):
            mid += change
            if isBadVersion(mid) != isBad:
                break
        if isBad:
            mid += 1
        return mid

if __name__ == "__main__":
    obj = Solution()
    print(obj.firstBadVersion(28))
    # print(obj.firstBadVersion(100000))
    # print(obj.firstBadVersion(900000))


