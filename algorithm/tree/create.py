#encoding=utf-8

from TreeNode import TreeNode

def binary_search_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    return root

def normal_tree():
    root = TreeNode(5)
    root.right = TreeNode(4)
    root.left = TreeNode(3)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(11)
    root.right.left = TreeNode(1)
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(12)
    root.right.right.left = TreeNode(12)
    root.left.right.right = TreeNode(16)
    return root

