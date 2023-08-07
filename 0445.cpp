class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> a, b;
        while (l1)
        {
            a.push_back(l1->val);
            l1 = l1->next;
        }
        while (l2)
        {
            b.push_back(l2->val);
            l2 = l2->next;
        }

        if (a.size() < b.size())
            a.insert(a.begin(), b.size() - a.size(), 0);
        if (b.size() < a.size())
            b.insert(b.begin(), a.size() - b.size(), 0);

        int carry = 0;
        ListNode* next = nullptr;
        for (int i = a.size() - 1; i >= 0; i--)
        {
            auto sum = carry + a[i] + b[i];
            carry = sum / 10;
            auto current = new ListNode(sum % 10, next);
            next = current;
        }

        if (carry > 0)
            next = new ListNode(carry, next);

        return next;
    }
};
