class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head)
            return nullptr;

        if (k == 0)
            return head;

        auto length = 0;
        auto current = head;
        ListNode* last = nullptr;
        while (current)
        {
            length++;
            last = current;
            current = current->next;
        }
        last->next = head;

        // no loops
        k %= length;
        // inverse
        k = length - k;

        last = head;
        while (--k > 0)
            last = last->next;

        auto result = last->next;
        last->next = nullptr;
        return result;
    }
};
