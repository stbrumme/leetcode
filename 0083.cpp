class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        auto current = head;

        while (current)
        {
            auto next = current->next;
            while (next && next->val == current->val)
                next = next->next;

            current->next = next;
            current = next;
        }

        return head;
    }
};
