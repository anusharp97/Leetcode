/*
Remove all elements from a linked list of integers that have value val.

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val)
{
    struct ListNode* prev = NULL;
    struct ListNode* temp;
    if (head == NULL)
        return NULL;
    struct ListNode* cur = head;
    while (cur!=NULL)
    {
        if (cur->val == val)
        {
            if (prev!=NULL)
            {
                temp = cur;
                prev->next = temp->next;
                cur = cur->next;
                free(temp);
            }
            else
            {
                head = cur->next;
                free(cur);
                cur = head;
            }
        }
        else
        {
            prev = cur;
            cur = cur->next;
        }
    }
    return head;
}
