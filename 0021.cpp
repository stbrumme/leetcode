class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1)
            return list2;
        if (!list2)
            return list1;

        ListNode* result = nullptr;
        if (list1->val < list2->val)
        {
            result = list1;
            list1 = list1->next;
        }
        else
        {
            result = list2;
            list2 = list2->next;
        }

        auto current = result;
        while (true)
        {
            if (!list1)
            {
                current->next = list2;
                return result;
            }
            if (!list2)
            {
                current->next = list1;
                return result;
            }

            if (list1->val < list2->val)
            {
                current->next = list1;
                list1 = list1->next;
            }
            else
            {
                current->next = list2;
                list2 = list2->next;
            }

            current = current->next;
        }

        return result;
    }
};

