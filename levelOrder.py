'''
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
def levelOrder(self, root: TreeNode) -> List[List[int]]:
  if root is None:
      return []
  traversal = []
  q = collections.deque()
  q.append(root)
  while q:
      size = len(q)
      t = []
      for i in range(size):
          cur= q.popleft()
          t.append(cur.val)
          if cur.left:
              q.append((cur.left))
          if cur.right:
              q.append((cur.right))
      traversal.append(t)
  return traversal
