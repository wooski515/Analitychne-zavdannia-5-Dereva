"""Задача 7. Мінімальна кількість камер для спостереження за всіма вузлами.

Жадібний обхід знизу вгору: камеру вигідно ставити не на листок, а на його
батька - так вона охопить більше вузлів. Кожен вузол повідомляє батькові
один з трьох станів.
"""

import sys

# Дерево може бути "ланцюжком" до 1000 вузлів - це впирається у стандартну межу рекурсії.
# Межу лише збільшуємо (max), щоб не зменшити її, якщо вона вже більша
sys.setrecursionlimit(max(sys.getrecursionlimit(), 10000))

NOT_COVERED = 0   # за вузлом ніхто не стежить
COVERED = 1       # за вузлом стежить камера нащадка, сам без камери
HAS_CAMERA = 2    # на вузлі стоїть камера


def min_camera_cover(root):
    """Повертає мінімальну кількість камер."""
    cameras = 0

    def dfs(node):
        nonlocal cameras
        if node is None:
            return COVERED   # порожній вузол не потребує спостереження
        left = dfs(node.left)
        right = dfs(node.right)
        if left == NOT_COVERED or right == NOT_COVERED:
            cameras += 1     # нащадок без нагляду - ставимо камеру тут
            return HAS_CAMERA
        if left == HAS_CAMERA or right == HAS_CAMERA:
            return COVERED   # за вузлом стежить камера нащадка
        return NOT_COVERED   # хай про цей вузол подбає батько

    if dfs(root) == NOT_COVERED:   # у кореня немає батька - камера на сам корінь
        cameras += 1
    return cameras
