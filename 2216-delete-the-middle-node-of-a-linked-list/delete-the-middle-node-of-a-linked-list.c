struct ListNode* deleteMiddle(struct ListNode* head) {
    if(head->next == NULL){
        return NULL; 
    }
    if(head->next->next == NULL){
        head->next = NULL; 
        return head; 
    }
    struct ListNode* prev = NULL;
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    int steps = 0; 
    
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;      
        steps++;  
    }

    prev->next = slow->next;

    return head;
}