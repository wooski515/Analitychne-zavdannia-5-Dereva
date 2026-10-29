"""Задача 8. Вертикальний обхід бінарного дерева.

Збираємо для кожного вузла трійку (стовпець, рядок, значення), сортуємо
трійки - отримуємо порядок за стовпцями, всередині стовпця зверху вниз,
а для однакової позиції - за значенням. Потім групуємо за стовпцями.
"""

import sys

# Дерево може бути "ланцюжком" до 1000 вузлів - це впирається у стандартну межу рекурсії.
# Межу лише збільшуємо (max), щоб не зменшити її, якщо вона вже більша
sys.setrecursionlimit(max(sys.getrecursionlimit(), 10000))


def vertical_traversal(root):
    """Повертає список стовпців зліва направо, у кожному - значення зверху вниз."""
    nodes = []

    def dfs(node, row, col):
        if node is None:
            return
        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)
    nodes.sort()
    result = []
    prev_col = None
    for col, row, val in nodes:
        if col != prev_col:   # почався новий стовпець
            result.append([])
            prev_col = col
        result[-1].append(val)
    return result
