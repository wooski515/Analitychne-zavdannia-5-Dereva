"""Задача 9. Відновити дерево з рядка preorder-обходу виду "1-2--3--4-5--6--7".

Кількість тире перед числом - глибина вузла. У стеку тримаємо шлях від
кореня до останнього доданого вузла: stack[d] - вузол на глибині d.
Для нового вузла глибини d його батько - stack[d - 1].
"""

from tree_node import TreeNode


def recover_from_preorder(traversal):
    """Повертає корінь відновленого дерева."""
    stack = []
    i = 0
    n = len(traversal)
    while i < n:
        depth = 0
        while i < n and traversal[i] == "-":   # рахуємо тире - це глибина
            depth += 1
            i += 1
        start = i
        while i < n and traversal[i].isdigit():   # читаємо число (може бути багатоцифровим)
            i += 1
        node = TreeNode(int(traversal[start:i]))
        while len(stack) > depth:   # піднімаємось до батька, що на глибині depth - 1
            stack.pop()
        if stack:
            parent = stack[-1]
            # Єдиний нащадок завжди лівий, тому спочатку заповнюємо left
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node
        stack.append(node)
    return stack[0]
