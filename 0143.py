class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        all = []
        current = head
        while current:
            all.append(current)
            current = current.next

        i = 0
        j = len(all) - 1
        while i < j:
            all[i].next = all[j]
            i += 1
            if i < j:
                all[j].next = all[i]
                j -= 1

        all[i].next = None

        return head
