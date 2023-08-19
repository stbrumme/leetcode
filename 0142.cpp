class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> seen;
        while (head)
        {
            if (seen.count(head) > 0)
                return head;
            seen.insert(head);
            head = head->next;
        }
        return nullptr;
    }
};
