from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# Solution to find the maximum depth of a binary tree
def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    # Recursively find the max depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    # Add 1 for the current node
    return 1 + max(left_depth, right_depth)

# Solution to find the lowest common ancestor in a Binary Search Tree
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Use BST properties to move left or right
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        # If p and q are on opposite sides or equal to root, root is LCA
        return root
