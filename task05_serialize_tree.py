"""Задача 5. Серіалізація та десеріалізація бінарного дерева.

Формат рядка - обхід у ширину, як у прикладах умови: "[1,2,3,null,null,4,5]".
"null" позначає відсутнього нащадка, зайві "null" у кінці не пишуться.
"""

from collections import deque

from tree_node import TreeNode


def serialize(root):
    """Перетворює дерево на рядок."""
    parts = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            parts.append("null")
        else:
            parts.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
    while parts and parts[-1] == "null":   # хвостові null нічого не додають
        parts.pop()
    return "[" + ",".join(parts) + "]"


def deserialize(data):
    """Відновлює дерево з рядка, отриманого від serialize, і повертає корінь."""
    parts = data.strip("[]").split(",") if data != "[]" else []
    if not parts:
        return None
    root = TreeNode(int(parts[0]))
    queue = deque([root])
    i = 1
    # Кожен вузол з черги отримує наступні два значення як лівого і правого нащадків
    while queue and i < len(parts):
        node = queue.popleft()
        if i < len(parts) and parts[i] != "null":
            node.left = TreeNode(int(parts[i]))
            queue.append(node.left)
        i += 1
        if i < len(parts) and parts[i] != "null":
            node.right = TreeNode(int(parts[i]))
            queue.append(node.right)
        i += 1
    return root
