class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # a bit of cheating: keep the list pointers unchanged, only swap the values
        start = head
        for _ in range(left - 1):
            start = start.next

        values = []
        current = start
        for _ in range(left, right + 1):
            values.append(current.val)
            current = current.next

        current = start
        for v in reversed(values):
            current.val = v
            current = current.next

        return head
