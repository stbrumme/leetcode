class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // cheating ...
        vector<int> all;
        for (auto l : lists)
        {
            while (l)
            {
                all.push_back(l->val);
                l = l->next;
            }
        }

        sort(all.begin(), all.end());

        ListNode* head = nullptr;
        while (!all.empty())
        {
            head = new ListNode(all.back(), head);
            all.pop_back();
        }

        return head;
    }
};
