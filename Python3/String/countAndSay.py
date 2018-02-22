# https://leetcode.com/problems/count-and-say/description/

# From Career Cup (http://www.careercup.com/question?id=4425679):
# "Count and Say problem" Write a code to do following:
# n                 String to print
# 0                 1
# 1                 1 1
# 2                 2 1
# 3                 1 2 1 1
# ...
# Base case: n = 0 print "1"
# for n = 1, look at previous string and write number of times a digit is seen and the digit itself. In this case, digit 1 is seen 1 time in a row... so print "1 1"
# for n = 2, digit 1 is seen two times in a row, so print "2 1"
# for n = 3, digit 2 is seen 1 time and then digit 1 is seen 1 so print "1 2 1 1"
# for n = 4 you will print "1 1 1 2 2 1"

# Consider the numbers as integers for simplicity. e.g. if previous string is "10 1" then the next will be "1 10 1 1" and the next one will be "1 1 1 10 2 1"

class Solution:
    # Time: O(n*2^n)
    # Space: O(2^n)
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return "1"
        curNums = ["1"]
        prevNums = []
        for _ in range(n - 1):
            charCounter = 1
            for i in range(1, len(curNums)):
                # When we get to a new number update and reset charCounter
                if curNums[i] != curNums[i - 1]:
                    prevNums.append(str(charCounter))
                    prevNums.append(curNums[i - 1])
                    charCounter = 1
                else:
                    charCounter += 1
            # If we've finished the current numbers, append the last piece
            prevNums.append(str(charCounter))
            prevNums.append(curNums[-1])
            # Copy the previous numbers into our current ones
            curNums = list(prevNums)
            del prevNums[:]
        return "".join(curNums)

    # Time: O(n*2^n)
    # Space: O(2^n)
    # This was my original solution, so keeping it I guess, but I like the above more
    # since we don't need the prevChar variable below and since strings are immutable,
    # we're just adding work for the garbage collector by reassigning prevChar repeatedly.
    # Also it's a bit clunky to do the "is not None" check
    def countAndSay2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return "1"
        curNums = ["1"]
        prevNums = []
        for _ in range(1,n):
            charCounter = 0
            prevChar = None
            for c in curNums:
                if prevChar != c and prevChar is not None:
                    prevNums.append(str(charCounter))
                    prevNums.append(prevChar)
                    charCounter = 1
                else:
                    charCounter += 1
                prevChar = c
            prevNums.append(str(charCounter))
            prevNums.append(prevChar)
            # Copy the previous numbers into our current list
            curNums = list(prevNums)
            del prevNums[:]
        return "".join(curNums)

if __name__ == "__main__":
    obj = Solution()
    print(obj.countAndSay(4)) # 1211