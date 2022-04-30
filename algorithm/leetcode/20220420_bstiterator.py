from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushleft(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.pushleft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def pushleft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

if __name__ == '__main__':
    tree20 = TreeNode(20)
    tree9 = TreeNode(9)
    tree15 = TreeNode(15, tree9, tree20)
    tree3 = TreeNode(3)
    tree7 = TreeNode(7, tree3, tree15)
    bstiterator = BSTIterator(tree7)
    print(bstiterator.next())
    print(bstiterator.next())
    print(bstiterator.hasNext())
    print(bstiterator.next())
    print(bstiterator.hasNext())
    print(bstiterator.next())
    print(bstiterator.hasNext())
    print(bstiterator.next())
    print(bstiterator.hasNext())