from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trim_bst(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < low:
            return self.trim_bst(root.right, low, high)
        if root.val > high:
            return self.trim_bst(root.left, low, high)
        if root.left is not None:
            root.left = self.trim_bst(root.left, low, high)
        if root.right is not None:
            root.right = self.trim_bst(root.right, low, high)
        return root


if __name__ == '__main__':
    tree2 = TreeNode(2)
    tree0 = TreeNode(0)
    tree = TreeNode(1, tree0, tree2)
    solve = Solution()
    answer = solve.trim_bst(tree, 1, 2)
    print(answer)
