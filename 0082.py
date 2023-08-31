class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def unique(node):
            if not node or not node.next:
                return True
            else:
                return node.val != node.next.val

        def skip(node):
            value = node.val
            while node and node.val == value:
                node = node.next
            return node


        while not unique(head):
            head = skip(head)

        lookahead = head
        while lookahead and lookahead.next:
            while not unique(lookahead.next):
                lookahead.next = skip(lookahead.next)
            lookahead = lookahead.next

        return head
