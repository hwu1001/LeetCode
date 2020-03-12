# https://leetcode.com/problems/decode-string/

class Solution:
    # DFS
    # Time: O(n)
    # Space: O(n)
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_string = []
        for c in s:
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = []
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_string = list(''.join(prev_str) + num*''.join(cur_string))
            elif c.isdigit():
                cur_num = cur_num*10 + int(c)
            else:
                cur_string.append(c)
        return ''.join(cur_string)

if __name__ == '__main__':
    s = '3[a2[c]]'
    # s = '3[a]2[bc]'
    # s = '2[abc]3[cd]ef'
    obj = Solution()
    print(obj.decodeString(s))