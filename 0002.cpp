class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> sum;
        int carry = 0;
        while (l1 || l2)
        {
            sum.push_back(carry);
            if (l1)
            {
                sum.back() += l1->val;
                l1 = l1->next;
            }
            if (l2)
            {
                sum.back() += l2->val;
                l2 = l2->next;
            }

            carry = sum.back() / 10;
            sum.back() %= 10;
        }

        if (carry > 0)
            sum.push_back(carry);

        ListNode* next = nullptr;
        for (int i = sum.size() - 1; i >= 0; i--)
        {
            auto current = new ListNode(sum[i], next);
            next = current;
        }
        return next;
    }
};
