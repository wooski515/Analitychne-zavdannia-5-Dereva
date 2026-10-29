"""Вузол бінарного дерева та перетворення дерева з масиву і назад.

Масив - це обхід дерева в ширину (по рівнях), де None - відсутній вузол,
як у прикладах умови: [1, None, 2, 3].
"""

from collections import deque


class TreeNode:
    """Вузол бінарного дерева."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Будує дерево з масиву і повертає корінь."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    """Перетворює дерево на масив у тому самому форматі (без зайвих None у кінці)."""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
