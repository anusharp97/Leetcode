'''
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

'''
def preorderTraversal(self, root: TreeNode) -> List[int]:
  stack = []
  traversal = []
  while stack or root:
      while root:
          stack.append(root)
          traversal.append(root.val)
          root = root.left
      root = stack.pop()
      root = root.right
  return traversal
