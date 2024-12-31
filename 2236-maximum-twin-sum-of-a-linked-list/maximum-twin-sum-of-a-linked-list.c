/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head->val;
    }
    if (head->next->next == NULL)
    {
        return head->val + head->next->val;
    }
    
    // Find the half on the linked list 
    struct ListNode *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) 
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Slow will be the head of the second linked list; we need to invert the second list
    struct ListNode *current = slow;
    struct ListNode *buffer = NULL, *prev = NULL;

    // Reverse the linked list
    while (current != NULL) { 
        buffer = current->next;
        current->next = prev;
        prev = current;
        current = buffer;
    }

    slow = prev;
    // Now, slow is the head of the second part
    int max = 0;
    current = head;
    while (slow != NULL)
    {
        if (current->val + slow->val > max)
        {
            max = current->val + slow->val;
        }
        current = current->next;
        slow    = slow->next;
        
    }
    return max;
}   