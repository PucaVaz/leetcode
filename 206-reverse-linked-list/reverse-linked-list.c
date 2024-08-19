/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* new_head = NULL;
    struct ListNode* aux = head;

    while (aux != NULL){
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = aux->val;
        new_node->next = new_head;
        new_head = new_node;
        aux = aux->next;
    }
    return new_head;
}