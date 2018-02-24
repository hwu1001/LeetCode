# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    # Time: O(n^2)
    # Space: O(n + u) - I could be wrong on this one, the space could be O(n^2), but since
    #                   we're not specifically given the input I believe it's just lower-case
    #                   characters so we store each character that appears once (which is constant
    #                   since there are only 26 characters possible) then we store the index of
    #                   each character found. So I think it would just be O(n), or O(n + u) where
    #                   u is some constant of the unique characters used in the substring
    # Hash table solution
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            return s == s[::-1]

        charIndices = {}
        begin = 0
        end = 0
        for i, char in enumerate(s):
            if char in charIndices:
                for index in charIndices[char]:
                    if i - index > end - begin and isPalindrome(s[index:i + 1]):
                        begin = index
                        end = i
                charIndices[char].append(i)
            else:
                charIndices[char] = [i]
        return s[begin:end + 1]
    
    # Time: O(n^2)
    # Space: O(1)
    # Check even/odd length substrings.
    # 
    # Knowing that a single character increase in our string can either make our 
    # palindrome 1 or 2 characters longer. (E.g., if we have the string "ce" and 
    # the character "c" is added at the end the palindrome has grown by 2. If we 
    # have "b" and add "b" the palindrome has grown by 1)
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0

        maxLen = 1
        start = 0
        for i in range(len(s)):
            # checkOdd = s[i - maxLen - 1:i + 1]
            # checkEven = s[i - maxLen:i + 1]
            # Check odd length strings
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            # Check even length strings
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start: start + maxLen]

    # Time: O(n^2) - This one appears to be truly O(n^2) - as it appears
    #                we'll expand around the center of each character in our
    #                given string
    # Space: O(1)
    # Expand around the center solution
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(s, left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            maxLen = max(len1, len2)
            if (maxLen > end - start):
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2
        return s[start:end + 1]

    # Time: O(n) - Finishes at most with 2*N steps
    # Space: O(n) - We store a transform of n characters plus sentinel characters
    #               then storage for the palindromic centers is equal to the length of the transform
    #               So roughly O(4*n), which is just O(n)
    # Manacher's Algorithm
    # There's a way to do this without the transformation, but it won't be as clean
    # as we'd have to handle several other conditions like expanding out from the
    # center of an even length string. Using the sentinels this problem can be avoided
    # https://articles.leetcode.com/longest-palindromic-substring-part-ii/
    # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
    def longestPalindrome4(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Transform S into T
        # For example, S = "abba", T = "^#a#b#b#a#$"
        def preProcess(s):
            if len(s) == 0:
                return ["^", "$"]
            ret = ["^"]
            for c in s:
                ret.append("#")
                ret.append(c)
            ret.append("#")
            ret.append("$")
            return ret
        
        transform = preProcess(s)
        # Initialize all palindromic centers to 0 (i.e., no palindromes longer than 1 character)
        paliCenters = [0] * len(transform)
        center = 0
        right = 0
        maxLen = 0
        centerIndex = 0
        for i in range(1, len(transform) - 1):
            iMirror = 2 * center - i # equals to i' = center - (i - center)
            if (right > i):
                paliCenters[i] = min(right - i, paliCenters[iMirror])
            # Atempt to expand palindrome centered at i
            while (transform[i + 1 + paliCenters[i]] == transform[i - 1 - paliCenters[i]]):
                paliCenters[i] += 1
            # If palindrome centered at i expand past right,
            # adjust center based on expanded palindrome
            if (i + paliCenters[i] > right):
                center = i
                right = i + paliCenters[i]
            # Update the max length found and our center index to get
            # the largest palindromic substring at the end of our loop
            if paliCenters[i] > maxLen:
                maxLen = paliCenters[i]
                centerIndex = i

        # We want to do start + maxLen for the second part of the slice
        # since the stop is not inclusive and maxLen is the length of our
        # longest found palindrome
        start = (centerIndex - 1 - maxLen) // 2
        return s[start : start + maxLen]

if __name__ == "__main__":
    # s = "babad"
    # s = "abba"
    # s = "abb"
    s = "racecar"
    # s = "cbbd"
    # s = "abcd"
    obj = Solution()
    print(obj.longestPalindrome2(s))
        