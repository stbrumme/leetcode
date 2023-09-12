class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        size = 0
        last = head
        while last:
            last = last.next
            size += 1

        # remove first
        mid = size // 2
        if mid == 0:
            return head.next

        # remove in the middle
        prev = head
        while mid > 1:
            prev = prev.next
            mid -= 1
        prev.next = prev.next.next

        return head
