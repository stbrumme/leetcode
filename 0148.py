class Solution:
    def bubble(self, head):
        # it's time for the most-hated algorithm: BUBBLESORT !!!
        again = True
        while again:
            again = False
            i = head
            while i.next:
                if i.val > i.next.val:
                    i.val, i.next.val = i.next.val, i.val
                    again = True
                i = i.next
        return head

    def insertion(self, head):
        # should be n log n, doesn't swap Node.val, only manipulates pointers

        done = None
        todo = head
        while todo:
            next = todo.next
            done = self.insertOne(done, todo)
            todo = next
        return done

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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # size == 0
            return None
        if not head.next: # size == 1
            return head

        size = 0
        i = head
        while i.next:
            size += 1
            i = i.next

        # let's try it hard way, without built-in sort routines ...
        if size < 20:
            head = self.bubble(head)  # O(n^2) ain't bad if n is small
        elif size < 1000:
            head = self.insertion(head)
        else:
            # list manipulation is just too slow, revert to Python's routines
            all = []
            i = head
            while i:
                all.append(i.val)
                i = i.next
            all.sort()
            i = head
            for a in all:
                i.val = a
                i = i.next

        return head

