class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> s;
        while (head)
        {
            s.push_back(head->val);
            head = head->next;
        }

        auto t = s;
        reverse(t.begin(), t.end());

        return s == t;
    }
};
