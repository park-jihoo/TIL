from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = None
        self.depth = None

    def deepest_leaves_sum(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.ans = 0

        def dfs(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                if self.depth < depth:
                    self.depth = depth
                    self.ans = root.val
                    return
                elif self.depth == depth:
                    self.ans += root.val
                    return
                else:
                    return
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)

        return self.ans


if __name__ == '__main__':
    tree7 = TreeNode(7)
    tree8 = TreeNode(8)
    tree4 = TreeNode(4, tree7, None)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6, None, tree8)
    tree2 = TreeNode(2, tree4, tree5)
    tree3 = TreeNode(3, None, tree6)
    tree1 = TreeNode(1, tree2, tree3)
    solve = Solution()
    print(solve.deepest_leaves_sum(tree1))
