class Solution:
    def insertOne(self, head, node):
        current = None
        if not head or node.val < head.val:
            node.next = head
            head = node
        else:
            current = head
            while current.next and current.next.val < node.val:
                current = current.next
            node.next = current.next
            current.next = node
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # taken from problem 148 (which I solved first)

        # should be n log n, doesn't swap Node.val, only manipulates pointers
        done = None
        todo = head
        while todo:
            next = todo.next
            done = self.insertOne(done, todo)
            todo = next
        return done
