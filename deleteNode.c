/* 450. Delete Node in a BST
 * Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
 * Return the root node reference (possibly updated) of the BST.
 * Basically, the deletion can be divided into two stages:
 * 
 * Search for a node to remove.
 * If the node is found, delete the node.
 * Note: Time complexity should be O(height of tree).
 * Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* deleteNode(struct TreeNode* root, int key)
{
    if (root == NULL)
    {
        return root;
    }
    struct TreeNode* parent = NULL;
    struct TreeNode* cur = root;
    struct TreeNode* temp;
    while(cur!=NULL)
    {
        if (cur->val == key)
            break;
        else if(cur->val<key)
        {
            parent = cur;
            cur = cur->right;
        }
        else
        {
            parent = cur;
            cur = cur->left;
        }
    }
    if (cur == NULL)
        return root;
    if (cur->left==NULL)
    {
        temp = cur->right;
    }
    else if(cur->right == NULL)
    {
        temp = cur->left;
    }
    else
    {
        struct TreeNode* successor = cur->right;
        while(successor->left!=NULL)
            successor = successor->left;
        successor->left = cur->left;
        temp = cur->right;
    }
    if (parent == NULL)
    {
        free(cur);
        return temp;
    }
    if (cur == parent->left)
    {
        parent->left = temp;
    }
    else
    {
        parent->right = temp;
    }
    free(cur);
    return root;
}
