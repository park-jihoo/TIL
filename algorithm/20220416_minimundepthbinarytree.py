from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.min_depth(root.right) + 1
        elif root.right is None:
            return self.min_depth(root.left) + 1
        else:
            return min(self.min_depth(root.right), self.min_depth(root.left)) + 1


if __name__ == '__main__':
    tree7 = TreeNode(7)
    tree15 = TreeNode(15)
    tree20 = TreeNode(20, tree15, tree7)
    tree9 = TreeNode(9)
    tree = TreeNode(3, tree9, tree20)
    solve = Solution()
    answer = solve.min_depth(tree)
    print(answer)
