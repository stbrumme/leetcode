class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto current = head;
        auto length = 0;
        while (current)
        {
            length++;
            current = current->next;
        }

        if (length == 0)
            return nullptr;
        if (n >  length)
            return head;
        if (n == length)
            return head->next;

        auto pos = length - n;

        current = head->next;
        auto prev = head;
        while (pos-- > 1 && current)
        {
            prev = current;
            current = current->next;
        }

        prev->next = current->next;
        return head;
    }
};
