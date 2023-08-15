class Solution:
    # swap two elements, return new left-most
    def two(self, root):
        if not root:
            return None
        if not root.next:
            return root

        left  = root
        right = root.next

        left.next  = right.next
        right.next = left

        return right


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        result = current = self.two(head)
        while current and current.next and current.next.next:
            current.next.next = self.two(current.next.next)
            current = current.next.next

        return result
