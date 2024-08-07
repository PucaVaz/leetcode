    /**
    * Definition for singly-linked list.
    * struct ListNode {
    *     int val;
    *     struct ListNode *next;
    * };
    */
    
    struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
        int sz = 0;
        struct ListNode *it;
        for (it = head; it != NULL; it = it->next) {
            sz++;
        }

        int rm = sz - n;
        it = head;
        struct ListNode *prev = NULL;
        for (int cnt = 0; cnt < rm; cnt++) {
            prev = it;
            it = it->next;
        }

        if (prev == NULL) {
            // remover a cabeça
            head = head->next;
        } else {
            prev->next = it->next;
        }

        free(it);
        return head;


    /*        
        struct ListNode* first = head;
        struct ListNode* second = head;

        int i = 0;

        while(i < n && first->next != NULL){
            first = first->next;
            i++;
        }

        while(first != NULL && first->next != NULL){
            first = first->next;
            second = second->next;
        }
        if (second->next != NULL)
        {
            struct ListNode * aux = second->next;
            second->next = second->next->next;
            free(aux);
        }
        else
        {
            struct ListNode * new_head = head->next;
            free(head);
            head = new_head;
            return head;
        }

        return head;
    */

    }
