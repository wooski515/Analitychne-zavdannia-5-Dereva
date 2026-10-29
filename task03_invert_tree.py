"""Задача 3. Інвертувати бінарне дерево (дзеркально відобразити)."""


def invert_tree(root):
    """Міняє місцями лівого і правого нащадків у кожному вузлі, повертає корінь."""
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
