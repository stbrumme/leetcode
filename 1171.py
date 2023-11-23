class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums = defaultdict()
        sums[0] = head

        # first pass: compute all sums and their latest occurrence
        node  = head
        total = 0
        while node:
            total += node.val
            sums[total] = node.next
            node = node.next

        # second pass: build new list with nodes from pass 1
        prehead = node = ListNode()
        total = 0
        while node:
            # basically identical loop
            total += node.val
            # except the following line has its left and right side reversed
            node.next = sums[total]
            node = node.next

        return prehead.next
