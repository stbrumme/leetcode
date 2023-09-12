class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # no change if length <= 2
        if not head or not head.next or not head.next.next:
            return head

        # find end of list
        last = head
        while last.next:
            last = last.next

        stop = head.next
        scan = head
        while True:
            # cut out even index
            even = scan.next
            scan.next = scan.next.next
            scan = scan.next

            # append to end
            even.next = None
            last.next = even
            last = last.next

            if scan == stop or scan.next == stop:
                return head
