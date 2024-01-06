class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # gather digits
        one  = ""
        scan = head
        while scan:
            one += str(scan.val)
            scan = scan.next

        # double
        sys.set_int_max_str_digits(0)
        two = str(2 * int(one))

        # prepend (at most) one digit
        if len(two) > len(one):
            head = ListNode(0, head)

        # overwrite values
        scan = head
        for c in two:
            scan.val = int(c)
            scan = scan.next

        return head
