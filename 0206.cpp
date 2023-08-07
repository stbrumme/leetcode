class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head)
            return nullptr;

        ListNode* prev = head;
        ListNode* current = head->next;
        head->next = nullptr;
        while (current)
        {
            auto next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        return prev;
    }
};
