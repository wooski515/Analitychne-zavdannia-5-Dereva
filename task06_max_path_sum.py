"""Задача 6. Максимальна сума шляху в бінарному дереві.

Для кожного вузла рахуємо gain - найбільшу суму шляху, що починається
в цьому вузлі й іде вниз в одне з піддерев. Шлях, що "згинається" у вузлі,
має суму node.val + gain(лівого) + gain(правого) - серед таких шукаємо максимум.
Від'ємний gain не беремо (краще не йти в те піддерево).
"""

import sys

# Дерево може бути "ланцюжком" до 30 000 вузлів, а стандартна межа рекурсії - 1000.
# Межу лише збільшуємо (max), щоб не зменшити її, якщо вона вже більша
sys.setrecursionlimit(max(sys.getrecursionlimit(), 100000))


def max_path_sum(root):
    """Повертає максимальну суму будь-якого непорожнього шляху."""
    best = root.val

    def gain(node):
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)   # шлях через node в обидва боки
        return node.val + max(left, right)          # вгору можна передати лише одну гілку

    gain(root)
    return best
