class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # build flat array
        stack = []
        while head:
            if head.val == 0 or stack[-1] == 0:
                stack.append(head.val) # next subsequence
            else:
                stack[-1] += head.val  # condense
            head = head.next

        # convert to linked list
        head = None
        for s in reversed(stack):
            if s > 0:
                head = ListNode(s, head)
        return head
