# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeVisualizer import TreeNode, deserialize

class Solution:
    # First pass - passed, but is slow.
    # Time: O(n^2) - Maybe? Since dictionaries are created for each node in the tree
    # Space: O(n) - It's more than O(n) but it's also not n^2 since we're not saving the whole tree
    #               for each node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        stack = [(root, 0, {root: 0})]
        p_ancestors = {}
        q_ancestors = {}
        while stack:
            node, depth, ancestors = stack.pop()
            if node.val == p.val:
                p_ancestors = dict(ancestors)
            if node.val == q.val:
                q_ancestors = dict(ancestors)
            if len(p_ancestors) > 0 and len(q_ancestors) > 0:
                break
            if node.right:
                a_right = dict(ancestors)
                a_right[node.right] = depth + 1
                stack.append((node.right, depth + 1, a_right))
            if node.left:
                a_left = dict(ancestors)
                a_left[node.left] = depth + 1
                stack.append((node.left, depth + 1, a_left))
        lca = None
        greatest_depth = -1
        for node in p_ancestors:
            if node in q_ancestors and q_ancestors[node] > greatest_depth:
                greatest_depth = q_ancestors[node]
                lca = node
        return lca

class Solution2:
    # Time: O(n) - Worst case visit all nodes
    # Space: O(h) - the height of the binary tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_tree(cur_node: TreeNode) -> bool:
            if not cur_node:
                return False
            left = recurse_tree(cur_node.left)
            right = recurse_tree(cur_node.right)
            mid = cur_node == p or cur_node == q
            if mid + left + right >= 2:
                self.ans = cur_node
            return mid or left or right

        self.ans = None
        recurse_tree(root)
        return self.ans

class Solution3:
    # Time: O(n) - Worst case visit all nodes
    # Space: O(n)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        parent = {root: None}
        # Find both nodes p and q in the tree, along with their parent nodes
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p: # find all ancestors for p
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q


if __name__ == '__main__':
    obj = Solution3()
    root = deserialize('[3,5,1,6,2,0,8,null,null,7,4]')
    assert(obj.lowestCommonAncestor(root, root.left, root.right) == root)
    assert(obj.lowestCommonAncestor(root, root.left, root.left.right.right) == root.left)