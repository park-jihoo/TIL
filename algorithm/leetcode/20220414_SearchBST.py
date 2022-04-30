from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if root.left is not None:
            left = self.search_bst(root.left, val)
            if left is not None:
                return left
        if root.right is not None:
            right = self.search_bst(root.right, val)
            if right is not None:
                return right
        return None

if __name__ == '__main__':
    tree5 = TreeNode(3)
    tree4 = TreeNode(1)
    tree3 = TreeNode(7)
    tree2 = TreeNode(2, tree4, tree5)
    tree1 = TreeNode(4, tree2, tree3)
    solve = Solution()
    answer = solve.search_bst(tree1, 2)
    print(answer, answer.val, answer.left, answer.right)