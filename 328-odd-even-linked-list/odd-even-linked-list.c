/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }
    
    struct ListNode* odd_head = head;
    struct ListNode* even_head = head->next;

    struct ListNode* odd_current = head;
    struct ListNode* even_current = head->next;

    while (even_current != NULL && even_current->next != NULL)
    {
        odd_current->next = odd_current->next->next;
        even_current->next = even_current->next->next;

        odd_current = odd_current->next;
        even_current = even_current->next;
    }
    odd_current->next = even_head;

    return odd_head;
}