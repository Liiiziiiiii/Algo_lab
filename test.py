import unittest

from main import TreeNode


class TestTreeNodeMethods(unittest.TestCase):
    def test_get_height(self):
        # Створення дерева для тестування
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(root.get_height(), 3)

    def test_diameter(self):
        # Створення дерева для тестування
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(root.diameter(), 4)

    def test_maximum_diameter(self):
        # Створення дерева для тестування
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(root.maximum_diameter(), 3)

if __name__ == '__main__':
    unittest.main()
