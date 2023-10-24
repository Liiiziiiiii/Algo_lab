class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Дані вузла
        self.left = left  # Ліва дитина
        self.right = right  # Права дитина

    def print_tree(self):
        print(self.val)
        # if self.left:
        #     self.left.val.print_tree()
        # if self.right:
        #     self.right.val.print_tree()

    def get_height(self):
        arr = []
        left = 0
        right = 0
        if self.left:
            left = self.left.get_height()
        if self.right:
            right = self.right.get_height()

        if self.val:
            arr.append(self.val)

        print(arr)

        return max(left, right) + 1

    def diameter(self):
        if self is None:
            return 0
        lheight = self.left.get_height() if self.left else 0
        rheight = self.right.get_height() if self.right else 0

        return lheight + rheight

    def maximum_diameter(self):
        left_diameter = self.left.diameter() if self.left else 0
        right_diameter = self.right.diameter() if self.right else 0

        return max(left_diameter, right_diameter)


if __name__ == '__main__':
    # root = TreeNode(10)
    #     # root.left = TreeNode(11)
    #     # root.left.left = TreeNode(2)
    #     # root.left.right = TreeNode(31)
    #     # root.right = TreeNode(12)
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.right.right = TreeNode(5)
    root.left.left.left.left = TreeNode(9)
    root.left.right.right.right = TreeNode(6)

    print("maximum_diameter:", root.maximum_diameter())
