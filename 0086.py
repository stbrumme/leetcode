class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        small = []
        big   = []

        current = head
        while current:
            if current.val < x:
                small.append(current.val)
            else:
                big.append(current.val)
            current = current.next

        current = head
        while current:
            if small:
                current.val = small[0]
                del small[0]
            else:
                current.val = big[0]
                del big[0]
            current = current.next

        return head
