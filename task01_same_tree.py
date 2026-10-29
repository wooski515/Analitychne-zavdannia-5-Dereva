"""Задача 1. Чи однакові два бінарні дерева."""


def is_same_tree(p, q):
    """Повертає True, якщо дерева p і q однакові за структурою та значеннями."""
    if p is None and q is None:
        return True
    if p is None or q is None:   # один вузол є, а іншого немає
        return False
    return (p.val == q.val
            and is_same_tree(p.left, q.left)
            and is_same_tree(p.right, q.right))
