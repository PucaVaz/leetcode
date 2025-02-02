class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_elements_1 = self.get_leaf_elements(root1)
        leaf_elements_2 = self.get_leaf_elements(root2)
        print(leaf_elements_1)
        print(leaf_elements_2)
        return leaf_elements_1 == leaf_elements_2

        
    def get_leaf_elements(self, root: Optional[TreeNode]):
        if root is None:
            return []
        
        stack = [root]

        leaf_elements = []

        while stack: 
            node = stack.pop()

            if node.left is None and node.right is None:
                leaf_elements.append(node.val)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return leaf_elements