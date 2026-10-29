"""Запуск усіх прикладів з умови завдання.

Запуск: python main.py
"""

import json

from task01_same_tree import is_same_tree
from task02_symmetric_tree import is_symmetric
from task03_invert_tree import invert_tree
from task04_kth_smallest import kth_smallest
from task05_serialize_tree import deserialize, serialize
from task06_max_path_sum import max_path_sum
from task07_binary_tree_cameras import min_camera_cover
from task08_vertical_traversal import vertical_traversal
from task09_recover_from_preorder import recover_from_preorder
from tree_node import build_tree, tree_to_list


def show(value):
    """Друк у форматі умови: null, true, false."""
    return json.dumps(value)


print("1. Те саме дерево")
for p, q in (([1, 2, 3], [1, 2, 3]), ([1, 2], [1, None, 2]), ([1, 2, 1], [1, 1, 2])):
    print(f"  Input: p = {show(p)}, q = {show(q)} -> Output: {show(is_same_tree(build_tree(p), build_tree(q)))}")

print("\n2. Симетричне дерево")
for values in ([1, 2, 2, 3, 4, 4, 3], [1, 2, 2, None, 3, None, 3], [1, 2, 1], [1, 1, 2]):
    print(f"  Input: root = {show(values)} -> Output: {show(is_symmetric(build_tree(values)))}")

print("\n3. Інвертувати бінарне дерево")
for values in ([4, 2, 7, 1, 3, 6, 9], [2, 1, 3], []):
    print(f"  Input: root = {show(values)} -> Output: {show(tree_to_list(invert_tree(build_tree(values))))}")

print("\n4. K-й найменший елемент у BST")
for values, k in (([3, 1, 4, None, 2], 1), ([5, 3, 6, 2, 4, None, None, 1], 3)):
    print(f"  Input: root = {show(values)}, k = {k} -> Output: {kth_smallest(build_tree(values), k)}")

print("\n5. Серіалізація та десеріалізація бінарного дерева")
for values in ([1, 2, 3, None, None, 4, 5], []):
    data = serialize(build_tree(values))
    restored = serialize(deserialize(data))
    print(f"  Input: root = {show(values)} -> serialize: {data} -> deserialize + serialize: {restored}")

print("\n6. Максимальна сума шляху")
for values in ([1, 2, 3], [-10, 9, 20, None, None, 15, 7]):
    print(f"  Input: root = {show(values)} -> Output: {max_path_sum(build_tree(values))}")

print("\n7. Камери бінарного дерева")
for values in ([0, 0, None, 0, 0], [0, 0, None, 0, None, 0, None, None, 0]):
    print(f"  Input: root = {show(values)} -> Output: {min_camera_cover(build_tree(values))}")

print("\n8. Вертикальний обхід бінарного дерева")
for values in ([3, 9, 20, None, None, 15, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 5, 7]):
    print(f"  Input: root = {show(values)} -> Output: {vertical_traversal(build_tree(values))}")

print("\n9. Відновити дерево після preorder-обходу")
for traversal in ("1-2--3--4-5--6--7", "1-2--3---4-5--6---7", "1-401--349---90--88"):
    print(f"  Input: traversal = {show(traversal)} -> Output: {show(tree_to_list(recover_from_preorder(traversal)))}")
