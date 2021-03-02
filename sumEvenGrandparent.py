'''
1315. Sum of Nodes with Even-Valued Grandparent
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:

https://assets.leetcode.com/uploads/2019/07/24/1473_ex1.png(Image)

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

'''

def sumEvenGrandparent(self, root: TreeNode) -> int:
  stack = []
  parent = None
  grandParent = None
  result = 0
  while stack or root:
      while root:
          stack.append((root,parent, grandParent))
          if grandParent and grandParent%2 == 0:
              result += root.val
          grandParent = stack[-1][1]
          parent = root.val
          root = root.left
      cur = stack.pop()
      grandParent = cur[1]
      parent = cur[0].val
      root = cur[0].right
  return result
