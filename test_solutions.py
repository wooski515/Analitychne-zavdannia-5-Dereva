"""Перевірка розв'язків на прикладах з умови та граничних випадках.

Запуск: python -m unittest -v
"""

import unittest

from task01_same_tree import is_same_tree
from task02_symmetric_tree import is_symmetric
from task03_invert_tree import invert_tree
from task04_kth_smallest import kth_smallest
from task05_serialize_tree import deserialize, serialize
from task06_max_path_sum import max_path_sum
from task07_binary_tree_cameras import min_camera_cover
from task08_vertical_traversal import vertical_traversal
from task09_recover_from_preorder import recover_from_preorder
from tree_node import TreeNode, build_tree, tree_to_list


def chain(length, val):
    """Вироджене дерево-ланцюжок: кожен вузол має лише лівого нащадка."""
    root = node = TreeNode(val)
    for _ in range(length - 1):
        node.left = TreeNode(val)
        node = node.left
    return root


class TestTrees(unittest.TestCase):
    def test_01_same_tree(self):
        self.assertTrue(is_same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3])))
        self.assertFalse(is_same_tree(build_tree([1, 2]), build_tree([1, None, 2])))
        self.assertFalse(is_same_tree(build_tree([1, 2, 1]), build_tree([1, 1, 2])))
        self.assertTrue(is_same_tree(build_tree([]), build_tree([])))

    def test_02_symmetric_tree(self):
        self.assertTrue(is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))
        self.assertFalse(is_symmetric(build_tree([1, 2, 2, None, 3, None, 3])))
        self.assertFalse(is_symmetric(build_tree([1, 2, 1])))
        self.assertFalse(is_symmetric(build_tree([1, 1, 2])))
        self.assertTrue(is_symmetric(build_tree([1])))
        self.assertTrue(is_symmetric(build_tree([])))

    def test_03_invert_tree(self):
        self.assertEqual(tree_to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))), [4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(tree_to_list(invert_tree(build_tree([2, 1, 3]))), [2, 3, 1])
        self.assertEqual(tree_to_list(invert_tree(build_tree([]))), [])
        self.assertEqual(tree_to_list(invert_tree(build_tree([1, 2]))), [1, None, 2])

    def test_04_kth_smallest(self):
        self.assertEqual(kth_smallest(build_tree([3, 1, 4, None, 2]), 1), 1)
        self.assertEqual(kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3), 3)
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual([kth_smallest(root, k) for k in range(1, 7)], [1, 2, 3, 4, 5, 6])

    def test_05_serialize_deserialize(self):
        for values in ([1, 2, 3, None, None, 4, 5], [], [1], [1, None, 2, None, 3], [-1000, 1000]):
            data = serialize(build_tree(values))
            self.assertEqual(tree_to_list(deserialize(data)), values)
        self.assertEqual(serialize(build_tree([1, 2, 3, None, None, 4, 5])), "[1,2,3,null,null,4,5]")
        self.assertEqual(serialize(None), "[]")

    def test_06_max_path_sum(self):
        self.assertEqual(max_path_sum(build_tree([1, 2, 3])), 6)
        self.assertEqual(max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])), 42)
        self.assertEqual(max_path_sum(build_tree([-3])), -3)
        self.assertEqual(max_path_sum(build_tree([-2, -1])), -1)
        self.assertEqual(max_path_sum(chain(30000, 1)), 30000)   # найглибше дерево з умови

    def test_07_binary_tree_cameras(self):
        self.assertEqual(min_camera_cover(build_tree([0, 0, None, 0, 0])), 1)
        self.assertEqual(min_camera_cover(build_tree([0, 0, None, 0, None, 0, None, None, 0])), 2)
        self.assertEqual(min_camera_cover(build_tree([0])), 1)
        self.assertEqual(min_camera_cover(chain(1000, 0)), 334)   # ланцюжок: камера на кожен 3-й вузол

    def test_08_vertical_traversal(self):
        self.assertEqual(vertical_traversal(build_tree([3, 9, 20, None, None, 15, 7])), [[9], [3, 15], [20], [7]])
        self.assertEqual(vertical_traversal(build_tree([1, 2, 3, 4, 5, 6, 7])), [[4], [2], [1, 5, 6], [3], [7]])
        self.assertEqual(vertical_traversal(build_tree([1, 2, 3, 4, 6, 5, 7])), [[4], [2], [1, 5, 6], [3], [7]])
        self.assertEqual(len(vertical_traversal(chain(1000, 0))), 1000)

    def test_09_recover_from_preorder(self):
        self.assertEqual(tree_to_list(recover_from_preorder("1-2--3--4-5--6--7")), [1, 2, 5, 3, 4, 6, 7])
        self.assertEqual(tree_to_list(recover_from_preorder("1-2--3---4-5--6---7")),
                         [1, 2, 5, 3, None, 6, None, 4, None, 7])
        self.assertEqual(tree_to_list(recover_from_preorder("1-401--349---90--88")),
                         [1, 401, None, 349, 88, 90])
        self.assertEqual(tree_to_list(recover_from_preorder("1000000000")), [1000000000])


if __name__ == "__main__":
    unittest.main()
