class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head
        next = current.next
        while next:
            middle = ListNode(gcd(current.val, next.val))
            middle.next = next
            current.next = middle

            current = next
            next = next.next

        return head
