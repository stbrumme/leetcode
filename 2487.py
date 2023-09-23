class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flat = []
        while head:
            flat.append(head.val)
            head = head.next

        threshold = 0
        result = None
        for f in reversed(flat):
            if f >= threshold:
                result = ListNode(f, result)
                threshold = f

        return result
