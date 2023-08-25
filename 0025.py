class Solution:
    def reverse(self, head, depth):
        if depth == 1:
            if head:
                head.next = None
            return head

        if not head or not head.next:
            return head

        result = self.reverse(head.next, depth - 1)
        head.next.next = head
        head.next = None
        return result

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head

        # not optimal ... split into chunks and reverse them
        parts = []
        current = head
        while current:
            next = current
            size = 0
            while next and size < k:
                next = next.next
                size += 1

            chunk = current
            if size == k:
                chunk = self.reverse(current, k)
            parts.append(chunk)
            current = next

        # merge all chunks
        tail = None
        for p in reversed(parts):
            last = p
            while last.next:
                last = last.next
            last.next = tail
            tail = p

        return tail
