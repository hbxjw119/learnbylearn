#encoding=utf-8

import create


def make_tree():
    return create.normal_tree()

# 最低公共祖先
def LCA(root, A, B):
    if root == None or root == A or root == B:
        return root
    left = LCA(root.left, A, B)
    right = LCA(root.right, A, B)
    if left != None and right != None:
        return root
    return left if left else right


# 二叉树所有路径
def tree_all_path(root):
    l = []
    if root:
        left_path = tree_all_path(root.left)
        right_path = tree_all_path(root.right)
        v = root.val
        if len(left_path) == 0 and len(right_path) == 0:
            l.append([v])
        else:
            if len(left_path) != 0:
                for i in left_path:
                    l.append('%s -> %s' % (v, i))
            if len(right_path) != 0:
                for j in right_path:
                    l.append('%s -> %s' % (v, j))


    return l

# 从根节点寻找到指定节点的路径
def find_a_path(root, node, p):
    if root is None:
        return root
    if root == node:
        p.append(root.val)
        print p
        return p
    p.append(root.val)
    if root.left:
        find_a_path(root.left, node, p)
        p.pop()
    if root.right:
        find_a_path(root.right, node, p)
        p.pop()


# 寻找最长路径
max_path = 0
def find_max_path(root):
    global max_path
    l, r = 0, 0
    if root is None:
        return 0
    if root.left:
        l = find_max_path(root.left) + 1
    if root.right:
        r = find_max_path(root.right) + 1
    cur_sum = l + r
    max_path = max(cur_sum, max_path)

    return max(l, r)

# 从根节点寻找最大路径和
pp = 0
def find_max_path_from_root(root, path):
    global pp
    if root is None:
        return 0
    path.append(root.val)
    if root.left is None and root.right is None:
        print path
        s = sum(path)

        pp = max(s, pp)

    if root.left:
        find_max_path_from_root(root.left, path)
        path.pop()
    if root.right:
        find_max_path_from_root(root.right, path)
        path.pop()
    return pp

def dfs2(root, path, node):
    if root is None:
        return
    if node == root:
        path.append(root)
        for i in path:
            print i.val
        return
    if root.left:
        path.append(root)
        dfs2(root.left, path, node)
        path.pop()
    if root.right:
        path.append(root)
        dfs2(root.right, path, node)
        path.pop()

# 寻找和为 target 的路径
def path_sum(root, target, path, s):
    if root is None:
        return path
    s.append(root.val)
    target -= root.val
    if target == 0 and root.left is None and root.right is None:
        path.append(list(s))
        #print path
    path_sum(root.left, target, path, s)
    path_sum(root.right, target, path, s)
    s.pop()
    return path


# 二叉搜索树的判别
# 方式：中序遍历二叉树，如果有序，则是二叉搜索树
# 常见的错误是，只判断了局部的二叉树搜索树特性，如下面的不是二叉搜索树
#      7
#     / \
#    4   9
#   /  \
#  3    10
pre_node = None
def is_bst(root):
    global pre_node
    if root:
        if not is_bst(root.left):
            return False

        if pre_node and root.val <= pre_node.val:
            return False
        pre_node = root

        if not is_bst(root.right):
            return False

    return True
if __name__ == '__main__':
    root = create.normal_tree()

