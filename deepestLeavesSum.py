'''
1302. Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''
def deepestLeavesSum(self, root: TreeNode) -> int:
  # level order traversal to find max depth
  if not root:
      return 0
  q = deque()
  q.append((root,1))
  maxDepth = -9999
  leafSum = 0
  while q:
      size = len(q)
      for i in range(size):
          root,depth = q.popleft()
          if depth == maxDepth:
              leafSum+=root.val
          else:
              leafSum = root.val
          maxDepth = max(depth,maxDepth)
          if root.left:
              q.append((root.left,depth+1))
          if root.right:
              q.append((root.right,depth+1))
  #print(maxDepth, leafSum)
  return leafSum
