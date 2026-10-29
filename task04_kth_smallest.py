"""Задача 4. k-й найменший елемент у бінарному дереві пошуку (BST).

Inorder-обхід (ліве - корінь - праве) BST дає значення у зростаючому
порядку, тому k-й відвіданий вузол і є відповіддю. Обхід зупиняється,
щойно відповідь знайдено.
"""


def kth_smallest(root, k):
    """Повертає k-те найменше значення (k рахується з 1)."""
    stack = []
    node = root
    while node or stack:
        while node:   # спускаємось до найменшого ще не відвіданого вузла
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return None   # k більше за кількість вузлів (за умовою не трапляється)
