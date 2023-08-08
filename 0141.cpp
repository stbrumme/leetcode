class Solution {
public:
    bool hasCycle(ListNode *head) {
        // don't wanna use the famous algorithm ...
        unordered_set<ListNode*> seen;
        while (head)
        {
            if (seen.count(head) > 0)
                return true;

            seen.insert(head);
            head = head->next;
        }

        return false;
    }
};
