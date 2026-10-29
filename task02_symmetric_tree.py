"""Задача 2. Чи є дерево симетричним (дзеркальним відносно центру)."""


def is_mirror(a, b):
    """Чи є піддерева a і b дзеркальними відображеннями одне одного."""
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    # Лівий нащадок a має дзеркалити правого нащадка b, і навпаки
    return (a.val == b.val
            and is_mirror(a.left, b.right)
            and is_mirror(a.right, b.left))


def is_symmetric(root):
    """Повертає True, якщо дерево симетричне."""
    if root is None:
        return True
    return is_mirror(root.left, root.right)
